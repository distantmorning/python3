from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://zh.moegirl.org/松冈祯丞"
f = requests.get(url)  # Get该网页从而获取该html内容
soup = BeautifulSoup(f.content, "lxml")  # 用lxml解析器解析该网页的内容, 好像f.text也是返回的html
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        for b in ul.find_all(name='b'):
            print(b.find_all(name='a'))
