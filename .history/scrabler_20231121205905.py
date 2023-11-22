import requests
import prettify
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama


colorama.init()
GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET
YELLOW = colorama.Fore.YELLOW

# initialize the set of links (unique links)
internal_urls = set()
external_urls = set()

def is_valid(url):
    """
    Проверяет, является ли url допустимым
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """
    Возвращает все найденные URL-адреса на `url, того же веб-сайта.
    """
    # все URL-адреса `url`
    urls = set()
    # доменное имя URL без протокола
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # пустой тег href
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # удалить параметры URL GET, фрагменты URL и т. д.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # недействительный URL
            continue
        if href in internal_urls:
            # уже в наборе
            continue
        if domain_name not in href:
            # внешняя ссылка
            if href not in external_urls:
                print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls
# количество посещенных URL-адресов будет сохранено здесь
total_urls_visited = 0
def crawl(url, max_urls=30):
    """
    Сканирует веб-страницу и извлекает все ссылки.
    Все ссылки будут в глобальных переменных набора external_urls и internal_urls.
    параметры:
        max_urls (int): максимальное количество URL-адресов для сканирования, по умолчанию 30
    """
    global total_urls_visited
    total_urls_visited += 1
    print(f"{YELLOW}[*] Crawling: {url}{RESET}")
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)

if __name__ == "__main__":
    crawl("https://rafi.moscow/")
    print("[+] Total Internal links:", len(internal_urls))
    print("[+] Total External links:", len(external_urls))
    print("[+] Total URLs:", len(external_urls) + len(internal_urls))
    print("[+] Total crawled URLs:", max_urls)
    

#url = 'https://rafi.moscow/'

#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'lxml')
#quotes = soup.find_all('img', alt='РАФИ|Главная')


#print(quotes)
#for job in quotes:
    #print("\n\n")
    #print(job)