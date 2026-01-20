import requests

from bs4 import BeautifulSoup

import json

import datetime

import numpy as np

import pandas as pd



# Function to fetch current BTC price from Coingecko

def get_btc_price():

    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

    response = requests.get(url)

    data = response.json()

    return data['bitcoin']['usd']



# Placeholder for Coinmetrics API (replace 'YOUR_API_KEY' with actual key for real use)

def get_coinmetrics_metric(metric, api_key):
    url = f"https://community-api.coinmetrics.io/v4/timeseries/asset-metrics?assets=btc&metrics={metric}&frequency=1d&api_key={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['data'][-1]['value'] if data['data'] else None
    except Exception as e:
        print(f"Error: {e}")
        return Nonee



# Scrape LookIntoBitcoin for approx values (e.g., Pi Cycle) - example for Pi Cycle

def scrape_lookintobitcoin(chart_url):

    response = requests.get(chart_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    # This is approximate; inspect site for exact selectors

    value_tag = soup.find('div', class_='chart-value')  # Placeholder selector

    return float(value_tag.text) if value_tag else None



# Power Law calculation (days since genesis: 2009-01-03)

def get_power_law_fair_value(price):

    genesis = datetime.date(2009, 1, 3)

    today = datetime.date.today()

    days = (today - genesis).days

    # Parameters from bitcoinpower.law: a ~ 10**-17, b ~5.82

    fair_value = 10**(-17) * (days ** 5.82)

    support = fair_value * 0.4  # Approx corridor

    resistance = fair_value * 1.6

    if price < support:

        return 1  # Buy

    elif price > resistance:

        return -1  # Sell

    else:

        return 0  # Hold



# Thresholds and scoring

def calculate_scores(data):

    scores = {}

    # RSI (assume weekly; fetch or input)

    rsi = data['rsi']

    scores['rsi'] = 1 if rsi < 30 else -1 if rsi > 70 else 0

    

    # LTH Supply %

    lth = data['lth_supply']

    scores['lth'] = 1 if lth > 75 else -1 if lth < 60 else 0

    

    # Pi Cycle (111DMA > 350DMA*2 = sell)

    pi_crossed = data['pi_crossed']  # 1 if crossed, else 0

    scores['pi'] = -1 if pi_crossed else 0

    

    # Heat Wave (assume 0-10 scale; >7 sell, <3 buy)

    heat = data['heat']

    scores['heat'] = 1 if heat < 3 else -1 if heat > 7 else 0

    

    # RUPL

    rupl = data['rupl']

    scores['rupl'] = 1 if rupl < 0.2 else -1 if rupl > 0.6 else 0

    

    # NUPL

    nupl = data['nupl']

    scores['nupl'] = 1 if nupl < 0 else -1 if nupl > 0.5 else 0

    

    # RHODL (high = sell)

    rhodl = data['rhodl']

    scores['rhodl'] = 1 if rhodl < 1 else -1 if rhodl > 100 else 0  # Adjust bands

    

    # Puell

    puell = data['puell']

    scores['puell'] = 1 if puell < 0.5 else -1 if puell > 4 else 0

    

    # MVRV Z-Score

    mvrv = data['mvrv']

    scores['mvrv'] = 1 if mvrv < 0 else -1 if mvrv > 7 else 0

    

    # SOPR (>1 rising = sell)

    sopr = data['sopr']

    scores['sopr'] = 1 if sopr < 1 else -1 if sopr > 1.5 else 0

    

    # Mayer Multiple

    mayer = data['mayer']

    scores['mayer'] = 1 if mayer < 1 else -1 if mayer > 2.4 else 0

    

    # Hash Ribbons (capitulation = buy)

    hash_ribbons = data['hash_ribbons']  # 1 if buy signal

    scores['hash'] = 1 if hash_ribbons else 0

    

    # 200WMA (price < MA = buy)

    wma200 = data['wma200']

    scores['wma200'] = 1 if price < wma200 else -1 if price > wma200 * 2 else 0

    

    # Power Law (weighted x2)

    power_score = get_power_law_fair_value(data['price'])

    scores['power'] = power_score * 2  # Double weight

    

    # Average score

    total_score = sum(scores.values()) / (len(scores) - 1 + 2)  # Adjust for power weight

    if total_score > 0.3:

        signal = "Buy"

    elif total_score < -0.3:

        signal = "Sell"

    else:

        signal = "Hold"

    return total_score, signal, scores



# Main execution

if __name__ == "__main__":

    price = get_btc_price()

    # Fetch or input data (replace with real fetches)

    data = {

        'price': price,

        'rsi': 50,  # Input or fetch from TradingView API

        'lth_supply': 78,  # From Glassnode 'supply/lth_supply'

        'pi_crossed': 0,  # Scrape or input

        'heat': 5,  # Input

        'rupl': get_coinmetrics_metric('indicators/rupl') or 0.3,

        'nupl': get_coinmetrics_metric('indicators/nupl') or 0.4,

        'rhodl': get_coinmetrics_metric('indicators/rhodl_ratio') or 10,

        'puell': get_coinmetrics_metric('indicators/puell_multiple') or 1.25,

        'mvrv': get_coinmetrics_metric('market/mvrv_z_score') or 2,

        'sopr': get_coinmetrics_metric('indicators/sopr') or 1.1,

        'mayer': scrape_lookintobitcoin('https://lookintobitcoin.com/charts/bitcoin-investor-tool/') or 1.8,

        'hash_ribbons': 1,  # Input buy signal

        'wma200': 50000,  # Approx, fetch from API

    }

    

    score, signal, details = calculate_scores(data)

    print(f"Current BTC Price: ${price}")

    print(f"Index Score: {score:.2f} -> {signal}")

    print("Details:", details)
