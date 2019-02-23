import requests
import re 
from lxml import etree
from bs4 import BeautifulSoup

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<li>(.*?)</',re.S)
    items = re.findall(pattern, html)
    print(items)
	
	
def main():
    url = 'https://www.mau2.com'
    html = get_one_page(url)
	print(html)


main()
	