import yfinance as yf
stock = yf.Ticker("AAPL")
historical_data = stock.history(period="15mo")
#historical_data.head(10)
current_value = historical_data.iloc[-1]["Close"]
current_date = historical_data.iloc[-1]["Date"]
