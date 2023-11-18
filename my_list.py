import yfinance as yf 
stock = yf.Ticker("AAPL") 
historical_data = stock.history(period="15mo") 
historical_data.head(10) 
