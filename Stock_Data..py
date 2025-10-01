import yfinance as yf
import pandas as pd
import json

#Extracting stock data
apple = yf.Ticker("AAPL")

#Stock Info
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    print(apple_info)

#Extracting share price
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()

#Reset Index of Dataframe
apple_share_price_data.reset_index(inplace=True)

#Plotting open price against Date
apple_share_price_data.plot(x="Date", y = "Open")

#Extracting Dividends
apple.dividends







