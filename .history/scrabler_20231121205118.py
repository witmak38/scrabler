import requests
import prettify
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def recursiveUrl(url, link, depth):
    if depth == 1:
        return url
    else:
        print(link['href'])
        page = requests.get(url + link['href'])
        soup = BeautifulSoup(page.text, 'html.parser')
        newlink = soup.find('a')
        if len(newlink) == 0:
            return link
        else:
            return link, recursiveUrl(url, newlink, depth + 1)

def getLinks(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        links.append(recursiveUrl(url, link, 0))
    return links

links = getLinks("https://rafi.moscow/")
print(links)
    
    
    

#url = 'https://rafi.moscow/'

#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
#for job in quotes:
    #print("\n\n")
    #print(job)