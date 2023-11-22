import requests
from bs4 import BeautifulSoup

url = 'https://rafi.moscow/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', alt_='')

print(quotes)
