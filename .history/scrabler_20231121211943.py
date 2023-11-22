import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama


for internal_link in internal_urls:
    #print(internal_link.strip())
    url = "https://rafi.moscow/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('img', alt='РАФИ|Главная')
    for job in quotes:
        print("\n\n")
        print(job)     
        
        
        
           
#url = 'https://rafi.moscow/'

#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
#for job in quotes:
    #print("\n\n")
    #print(job)