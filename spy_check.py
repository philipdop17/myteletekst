import yfinance as yf
import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

spy = yf.Ticker("SPY", session=session)
print(spy.info['symbol'])
