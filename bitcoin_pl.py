import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical data for Bitcoin
bitcoin_data = yf.download('ETH-USD', start='2020-01-01', end='2025-01-21')

# Plot the closing prices
plt.figure(figsize=(12, 6))
plt.plot(bitcoin_data['Close'], label='Bitcoin Price')
plt.title('Historical Bitcoin Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()
