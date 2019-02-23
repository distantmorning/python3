import requests
import urllib
from bs4 import BeautifulSoup

def get_one_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

def main():
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    url2 = 'https://zh.moegirl.org/水瀨祈'
    #url3 = 'https://www.mau2.com/'
    html = requests.get(url2,headers= headers).text
    soup = BeautifulSoup(html,'lxml')
    print(soup.p)
main()