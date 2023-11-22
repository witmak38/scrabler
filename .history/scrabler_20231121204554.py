import requests
import prettify
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

int_url = set()
ext_url = set()

def valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Возвращаем все URL-адреса
def website_links(url):
    urls = set()
    # извлекаем доменное имя из URL
    domain_name = urlparse(url).netloc
    # скачиваем HTML-контент вэб-страницы
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
for a_tag in soup.findAll("a"):
    href = a_tag.attrs.get("href")
    if href == "" or href is None:
        # href пустой тег
        continue    
    

#url = 'https://rafi.moscow/'

#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
#for job in quotes:
    #print("\n\n")
    #print(job)