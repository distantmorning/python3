import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def getTwo(userA, userB):
    dictAB = {}
    pattern3 = re.compile('————《<a href=".*?" title=".*?">(.*?)</a>》', re.S)
    htmlA = requests.get("https://zh.moegirl.org/zh-cn/" + userA, headers=headers)
    htmlB = requests.get("https://zh.moegirl.org/zh-cn/" + userB, headers=headers)
    titleA = re.findall(pattern3, htmlA.text)
    titleB = re.findall(pattern3, htmlB.text)
    for itA in titleA:
        for itB in titleB:
            if (itA == itB):
                dictAB[itA] = 1
    return dictAB


wTitles = getTwo("水濑祈", "松冈祯丞")
for w in wTitles:
        print(w)