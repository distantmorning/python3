import requests
from lxml import etree
import re
from retry import retry
import tool
proxies = tool.getProxies()
headers = tool.getHeaders()
#url = 'https://ja.wikipedia.org/wiki/%E6%B0%B4%E7%80%AC%E3%81%84%E3%81%AE%E3%82%8A'
url = 'https://ja.wikipedia.org/wiki/佐倉綾音'
html = etree.HTML(requests.get(url, proxies=proxies).text)
result = html.xpath('//*[@id="mw-content-text"]/div//dl[position()<2]/dd//ul/li/a/text()')
#result2 = html.xpath('//*[@id="mw-content-text"]/div//dl[position()<2]/dd//ul/li/a/@href')
allcast = {}
@retry()
def getContent(url):
    r = requests.get(url2, proxies=proxies).text
    return r

for i in result:
    url2 = 'https://ja.wikipedia.org/wiki/' + i
    #html = etree.HTML(requests.get(url2, proxies=proxies).text)
    # result3 = re.search('<th>音響監督.*?title="(.*?)">.*?<th>アニメーション制作.*?title=".*?">(.*?)</a>',requests.get(url2, proxies=proxies).text, re.S)
    target = getContent(url2)
    #yinjian = re.search('音響監督.*?title="(.*?)"',target, re.S)
    casts = re.findall('声.*?title="(.*?)"',target, re.S)
    if casts:
        for na in casts:
            if na not in allcast.keys():
                allcast[na] = 1
            else:
                allcast[na] = allcast.get(na) + 1


for ke in allcast.keys():
    with open('cast.txt', 'a', encoding='utf-8') as file:
        file.write(ke + "\t" + str(allcast.get(ke)) + "\n")


