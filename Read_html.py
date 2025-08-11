import pandas as pd
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'

read_html_pandas_data = pd.read_html(url)
print(read_html_pandas_data)

#or we can also do by soup 
#read_html_pandas_data = pd.read_html(str(soup))

netflix_dataframe = read_html_pandas_data[0]
final = read_html_pandas_data.head()
print(final)
