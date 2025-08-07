import requests
from bs4 import BeautifulSoup
page = requests.get("https://en.wikipedia.org/wiki/Main_Page").text

#Creates bs object
soup = BeautifulSoup(page, "html.parser")

#Pulls all instances of <a> tag
artists = soup.find_all('a')

#Clears data of all tags
for artist in artists :
    names = artist.contents[0]
    fulllink = artist.get('href')
print(soup.prettify())    