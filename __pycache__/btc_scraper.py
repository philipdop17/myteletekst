import requests
import json

def fetch_btc_data():
    url = "https://scanner.tradingview.com/crypto/scan"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    payload = {
        "symbols": {
            "tickers": ["BINANCE:BTCUSDT"],
            "query": {"types": []}
        },
        "columns": [
            "close",           # Current price
            "RSI|14",          # RSI (14-day)
            "SMA200",          # 200-day simple moving average
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        data = response.json()
        btc_data = data["data"][0]["d"]
        return {
			"price": btc_data[0] if btc_data[0] is not None else 120000,
			"rsi": btc_data[1] if btc_data[1] is not None else 50,
			"sma200": btc_data[2] if btc_data[2] is not None else 50000

        }
    except Exception as e:
        print(f"Error fetching BTC data: {e}")
        return {
            "price": 120000,
            "rsi": 50,
            "sma200": 50000
        }
