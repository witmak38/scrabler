import requests
import prettify
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

url = 'https://rafi.moscow/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
for job in quotes:
    print("\n\n")
    print(job)