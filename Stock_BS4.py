import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore", category = FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

data = requests.get(url).text


soup = BeautifulSoup(data, 'html.parser')


netflix_data = pd.DataFrame(columns=['Open','Date','High','Low','Close','Volume'])


for row in soup.find("tbody").find_all('tr'):
    col = row.find_all('td')
    date = col[0].text
    open_price = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    volume = col[5].text
    adj_close = col[6].text

    netflix_data = pd.concat(
        [netflix_data, pd.DataFrame({
            "Date": [date],
            "Open": [open_price],
            "High": [high],
            "Low": [low],
            "Close": [close],
            "Volume": [volume],
            "Adj": [adj_close]
        })],
        ignore_index=True
    )
    data_final = netflix_data.head()
print(data_final)

