import requests
import datetime

# Function to fetch current BTC price from Coingecko
def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['usd']
    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Error fetching BTC price: {e}. Using fallback price.")
        return 120000  # Fallback price

# Function to fetch metrics from CryptoCompare (only price for now)
def get_crypto_metric_from_cryptocompare(metric):
    url_map = {
        'price': "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD",
        # Add more endpoints if needed
    }
    url = url_map.get(metric)
    if not url:
        print(f"No mapping for {metric}")
        return None
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get('USD')
    except Exception as e:
        print(f"Error fetching {metric}: {e}")
        return None

# Placeholder for scraping LookIntoBitcoin
def scrape_lookintobitcoin(chart_url):
    print(f"Warning: Scraping not implemented for {chart_url}. Using fallback value.")
    return None

# Power Law calculation
def get_power_law_fair_value(price):
    genesis = datetime.date(2009, 1, 3)
    today = datetime.date.today()
    days = (today - genesis).days
    fair_value = 10**(-17) * (days ** 5.82)
    support = fair_value * 0.4
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
    price = data['price']
    scores['rsi'] = 1 if data['rsi'] < 30 else -1 if data['rsi'] > 70 else 0
    scores['lth'] = 1 if data['lth_supply'] > 75 else -1 if data['lth_supply'] < 60 else 0
    scores['pi'] = -1 if data['pi_crossed'] else 0
    scores['heat'] = 1 if data['heat'] < 3 else -1 if data['heat'] > 7 else 0
    scores['rupl'] = 1 if data['rupl'] < 0.2 else -1 if data['rupl'] > 0.6 else 0
    scores['nupl'] = 1 if data['nupl'] < 0 else -1 if data['nupl'] > 0.5 else 0
    scores['rhodl'] = 1 if data['rhodl'] < 1 else -1 if data['rhodl'] > 100 else 0
    scores['puell'] = 1 if data['puell'] < 0.5 else -1 if data['puell'] > 4 else 0
    scores['mvrv'] = 1 if data['mvrv'] < 0 else -1 if data['mvrv'] > 7 else 0
    scores['sopr'] = 1 if data['sopr'] < 1 else -1 if data['sopr'] > 1.5 else 0
    scores['mayer'] = 1 if data['mayer'] < 1 else -1 if data['mayer'] > 2.4 else 0
    scores['hash'] = 1 if data['hash_ribbons'] else 0
    scores['wma200'] = 1 if price < data['wma200'] else -1 if price > data['wma200'] * 2 else 0
    scores['power'] = get_power_law_fair_value(price) * 2
    num_scores = len(scores) - 1 + 2
    total_score = sum(scores.values()) / num_scores
    signal = "Buy" if total_score > 0.3 else "Sell" if total_score < -0.3 else "Hold"
    return total_score, signal, scores

# Main execution
# Main execution
# Main execution
if __name__ == "__main__":
    from btc_scraper import fetch_btc_data

    btc_metrics = fetch_btc_data()
    print("Raw BTC data:", btc_metrics)

    price = btc_metrics['price']
    data = {
        'price': price,
        'rsi': btc_metrics['rsi'],
        'lth_supply': 78,
        'pi_crossed': 0,
        'heat': 5,
        'rupl': 0.3,
        'nupl': 0.4,
        'rhodl': 10,
        'puell': 1.25,
        'mvrv': 2,
        'sopr': 1.1,
        'mayer': scrape_lookintobitcoin('https://www.lookintobitcoin.com/charts/bitcoin-investor-tool/') or 1.8,
        'hash_ribbons': 1,
        'wma200': btc_metrics['sma200'],
    }

    score, signal, details = calculate_scores(data)
    print(f"Current BTC Price: ${price:,}")
    print(f"Index Score: {score:.2f} -> {signal}")
    print("Details:", details)



    score, signal, details = calculate_scores(data)
    print(f"Current BTC Price: ${price:,}")
    print(f"Index Score: {score:.2f} -> {signal}")
    print("Details:", details)
