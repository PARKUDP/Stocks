import yfinance as yf

coke = yf.Ticker("COKE")
print(coke.info)
ticker_info = yf.Ticker("9984.T")
