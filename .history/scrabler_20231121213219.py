import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

# запускаем модуль colorama

colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

# инициализировать set's для внутренних и внешних ссылок (уникальные ссылки)
internal_urls = set()
external_urls = set()

total_urls_visited = 0

domain_name = "rafi.moscow"
# сохранить внутренние ссылки в файле
'''
with open(f"{domain_name}_internal_links.txt", "r") as f:
    for internal_link in internal_urls:
        print(internal_link.strip(), file=f)
'''       
        
# получим объект файла
file = open("{domain_name}_internal_links.txt", "r")

while True:
    # считываем строку
    line = file1.readline()
    # прерываем цикл, если строка пустая
    if not line:
        break
    # выводим строку
    print(line.strip())

# закрываем файл
file1.close

#for internal_link in internal_urls:
    #print(internal_link.strip())

for internal_link in internal_urls:
    #print(internal_link.strip())
    print(f"{GREEN}[*] Страница: {internal_link.strip()}{RESET}")
    url = internal_link.strip()
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('img', alt='')
    for job in quotes:
        print("\n\n")
        print(job['src'])     
        
        
        
           
#url = 'https://rafi.moscow/'

#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
#for job in quotes:
    #print("\n\n")
    #print(job)