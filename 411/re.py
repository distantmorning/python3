import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


def getCast(name):
    s = requests.get("https://zh.moegirl.org/zh-cn/" + name, headers=headers).text
    html = etree.HTML(s)
    result = html.xpath('//ul/li[position()<last()-1]/a/text()')
    for tes in result:
        print(tes)


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


def getBaidu(userA, userB):
    dicA = getTitles(userA)
    dibB = getTitles(userB)
    for a in dicA:
        for b in dibB:
            if (a == b):
                print(a)


def getTitles(name):
    url = "https://baike.baidu.com/item/" + name
    html = requests.get(url, headers=headers).text
    str = html.encode("iso-8859-1").decode('utf-8')
    html = etree.HTML(str)
    titles = {}
    result = html.xpath('//table[@log-set-param="table_view"]//div//a/text()')
    for tes in result:
        titles[tes] = 1
    return titles


def getBuCast(title):
    url = "https://baike.baidu.com/item/" + title
    html = requests.get(url, headers=headers).text
    str = html.encode("iso-8859-1").decode('utf-8')
    titles = {}
    if (str == ''):
        return titles
    else:
        html = etree.HTML(str)
        result = html.xpath('//dd[@class="basicInfo-item value"]//a/text()')
        for tes in result:
            titles[tes] = 1
        return titles


wTitles = getTwo("水濑祈", "水濑祈")
for w in wTitles:
    one = getBuCast(w)
    for p in one:
        print(p)
