import yfinance as yf
stock = yf.Ticker("AAPL")
historical_data = stock.history(period="15mo")
#historical_data.head(10)
current_value = historical_data.iloc[-1]["Close"]
current_date = historical_data.iloc[-1]["Date"]
six_months_back_close = historical_data.iloc[0]["Close"]
six_months_back_date = historical_data.iloc[0]["Date"]
one_month_back_close = historical_data.iloc[-20]["Close"]  # Approx. 1 month data
one_month_back_date = historical_data.iloc[-20]["Date"]
