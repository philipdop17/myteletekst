import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Fetch BTC/ETH data (use Yahoo finance for example)
crypto_data = yf.download("BTC-USD", start="2015-01-01", end=datetime.today().strftime('%Y-%m-%d'))

# Moving Average calculation (10-month MA for trend regime filter)
crypto_data['MA10'] = crypto_data['Adj Close'].rolling(window=30).mean()  # 10-month moving average

# Weekly momentum score function (simple example using 5/20 SMA and RSI)
def calculate_momentum(data):
    # Calculate moving averages
    data['SMA5'] = data['Adj Close'].rolling(window=5).mean()
    data['SMA20'] = data['Adj Close'].rolling(window=20).mean()
    
    # Calculate RSI (14)
    delta = data['Adj Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Momentum score
    data['momentum_score'] = ((data['SMA5'] > data['SMA20']) * 25 + (data['RSI'] > 50) * 25)
    return data

crypto_data = calculate_momentum(crypto_data)

# Backtesting logic (for simplicity, just track positions and P&L)
initial_cash = 100000
cash = initial_cash
position = 0
positions_history = []

# Define option hedging (simplified, just monitor buying/selling puts/calls based on trend)
def hedge_position(price, risk_off):
    if risk_off:
        return 0  # Exit position during RISK-OFF
    else:
        # Buy puts (simplified: always buy 5% OTM puts)
        return max(0, price * 0.95)  # Protective put, 5% OTM

# Define the backtest loop
for i in range(30, len(crypto_data)):
    current_data = crypto_data.iloc[i]
    prev_data = crypto_data.iloc[i - 1]

    # Step 1: Calculate Trend (RISK-ON or RISK-OFF)
    risk_off = current_data['Adj Close'] < current_data['MA10']
    
    # Step 2: Determine Position Size Based on Momentum Score
    momentum_score = current_data['momentum_score']
    
    if risk_off:
        position = 0
        # Cash management on RISK-OFF (move into defensive assets)
        cash *= 1  # No change in cash as we assume 100% cash allocation
    else:
        if momentum_score > 70:
            position = cash / current_data['Adj Close']
            cash = 0  # All cash used for crypto
        elif momentum_score > 50:
            position = 0.7 * (cash / current_data['Adj Close'])
            cash = 0.3 * cash
        elif momentum_score > 30:
            position = 0.4 * (cash / current_data['Adj Close'])
            cash = 0.6 * cash
        else:
            position = 0
            cash = 0  # No crypto position

    # Step 3: Hedge (Options strategy — Simplified)
    if position > 0:
        hedge_price = hedge_position(current_data['Adj Close'], risk_off)
        # Simulate buying/selling options to reduce risk or boost upside
        print(f"Position: {position} units, Hedge Price: {hedge_price}")
    
    # Step 4: Log performance
    portfolio_value = position * current_data['Adj Close'] + cash
    positions_history.append(portfolio_value)

# Convert history to DataFrame and plot results
portfolio_history = pd.DataFrame(positions_history, columns=["Portfolio Value"], index=crypto_data.index[30:])
portfolio_history['Portfolio Value'].plot(figsize=(10, 6), title="Portfolio Value Over Time")
plt.show()

# Print final result
final_value = portfolio_history['Portfolio Value'].iloc[-1]
print(f"Final Portfolio Value: ${final_value:.2f}")
