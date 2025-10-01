import yfinance as yf
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def make_graph(stock_data, revenue_data, stock_label='Stock Price', revenue_label='Revenue', title='Tesla Stock and Revenue'):
    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plot stock price
    ax1.set_xlabel('Date')
    ax1.set_ylabel(stock_label, color='blue')
    ax1.plot(stock_data['Date'], stock_data['Close'], color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Plot revenue on a secondary axis
    ax2 = ax1.twinx()
    ax2.set_ylabel(revenue_label, color='red')
    ax2.plot(revenue_data['Date'], revenue_data['Revenue'].astype(float), color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Title and layout
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    fig.tight_layout()
    plt.show()

tesla_data = yf.download('TSLA', start="2010-01-01", end="2021-06-30")
tesla_data.reset_index(inplace=True)  # reset index so "Date" is a column

url = " https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data,'html.parser')
tesla_revenue = pd.DataFrame(columns=['Date','Revenue'])
table = soup.find_all("tbody")[1]
for row in table.find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({ 
    "Date" : [date],
    "Revenue": [revenue]
})],
                          ignore_index = True)
# Remove commas, dollar signs, and strip whitespace
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$',"", regex=True).str.strip()

# Drop empty strings
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Convert to numeric
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].astype(float)

# Convert Date to datetime
tesla_revenue["Date"] = pd.to_datetime(tesla_revenue["Date"])



tesla_revenue.dropna(inplace=True)

tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
Tesla_revenue = tesla_revenue.tail()


make_graph(tesla_data, tesla_revenue, title="Tesla Stock Price and Revenue (up to June 2021)")
