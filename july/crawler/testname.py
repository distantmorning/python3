import requests
from lxml import etree
import re
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）

#url = 'https://ja.wikipedia.org/wiki/%E6%B0%B4%E7%80%AC%E3%81%84%E3%81%AE%E3%82%8A'
url = 'https://ja.wikipedia.org/wiki/松岡禎丞'
html = etree.HTML(requests.get(url, proxies=proxies).text)
result = html.xpath('//*[@id="mw-content-text"]/div//dl[position()<2]/dd//ul/li/a/text()')
#result2 = html.xpath('//*[@id="mw-content-text"]/div//dl[position()<2]/dd//ul/li/a/@href')
for i in result:
    print(i)
print(len(result))

url2 = 'https://ja.wikipedia.org/wiki/' + 'Re:ゼロから始める異世界生活'
url22 = 'https://ja.wikipedia.org/wiki/' + 'CHAOS;CHILD'

result2 = re.search('<th>音響監督.*?title="(.*?)">.*?<th>アニメーション制作.*?title=".*?">(.*?)</a>',requests.get(url2, proxies=proxies).text, re.S)

if result2:
    print(i + "\t" + result2.group(1) + "\t" + result2.group(2))
else:
    print(23)