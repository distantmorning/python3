import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

def getTwo(userA, userB):
    dictAB = {}
    pattern3 = re.compile('————《<a href=".*?" title=".*?">(.*?)</a>》', re.S)
    htmlA = requests.get("https://zh.moegirl.org/zh-cn/" + userA)
    htmlB = requests.get("https://zh.moegirl.org/zh-cn/" + userB)
    titleA = re.findall(pattern3, htmlA.text)
    titleB = re.findall(pattern3, htmlB.text)
    for itA in titleA:
        for itB in titleB:
            if (itA == itB):
                dictAB[itA] = 1
    return dictAB



wTitles = getTwo("水濑祈", "本渡枫")
for w in wTitles:
    print(w)
print(len(wTitles))