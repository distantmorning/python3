import requests
from lxml import etree
import re
import tool
import linecache
proxies = tool.getProxies()
headers = tool.getHeaders()
com = []
st = linecache.getlines('tgtg.txt')

for s in st:
    com.append(s[0:-1])
#url = 'https://ja.wikipedia.org/wiki/%E6%B0%B4%E7%80%AC%E3%81%84%E3%81%AE%E3%82%8A'
url = 'https://ja.wikipedia.org/wiki/水瀬いのり'
html = etree.HTML(requests.get(url, proxies=proxies).text)
result = html.xpath('//*[@id="mw-content-text"]/div//dl[position()<2]/dd//ul/li/a/text()')

for na in com:
    count = []
    url2 = 'https://ja.wikipedia.org/wiki/' + na
    html2 = etree.HTML(requests.get(url2, proxies=proxies).text)
    result2 = html2.xpath('//*[@id="mw-content-text"]/div//dl[position()<2]/dd//ul/li/a/text()')
    for i in result2:
        for j in result:
            if i == j:
                count.append(i)
    print(na + "\t" + str(len(count)))

