import requests
import prettify
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


listUrl = []

def recursiveUrl(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    if links is None or len(links) == 0:
        listUrl.append(url)
        print(url)
        return 1;
    else:
        listUrl.append(url)
        print(url)
        for link in links:
            #print(url+link['href'][1:])
            recursiveUrl(url+link['href'][1:])


recursiveUrl('https://rafi.moscow/')
print(listUrl)
    
    
    

#url = 'https://rafi.moscow/'

#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
#for job in quotes:
    #print("\n\n")
    #print(job)