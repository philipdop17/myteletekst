import yfinance as yf
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Fetch SPY options data
spy = yf.Ticker("SPY")
data = spy.history(period="2y")  # Add IV, volume features here
data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)  # Binary: up/down

X = data[['Open', 'High', 'Low', 'Volume']]  # Expand features
y = data['Target']
X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2)

model = xgb.XGBClassifier(objective='binary:logistic')
model.fit(X_train, y_train)
preds = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, preds):.2f}")
