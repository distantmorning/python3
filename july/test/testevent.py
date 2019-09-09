import requests
from lxml import etree
import re
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）

dict = {}
for page in range(1,23):
    url = 'https://www.eventernote.com/actors/%E6%9D%BE%E5%B2%A1%E7%A6%8E%E4%B8%9E/2651/events?actor_id=2651&limit=20&page=' + str(page)
    html = etree.HTML(requests.get(url, proxies=proxies).text)
    result = html.xpath('/html/body/div[2]/div/div[2]/div[2]/ul//li/div[1]/p[1]/text()[1] | /html/body/div[2]/div/div[2]/div[2]/ul//li/div[2]/h4/a/text()')
    for i in range(1,len(result)+1):
        if i%2 ==1:
            dict[i] = result[i-1]


for page in range(1,25):
    url = 'https://www.eventernote.com/actors/%E6%B0%B4%E7%80%AC%E3%81%84%E3%81%AE%E3%82%8A/2890/events?actor_id=2890&limit=20&page=' + str(page)
    html = etree.HTML(requests.get(url, proxies=proxies).text)
    result = html.xpath('/html/body/div[2]/div/div[2]/div[2]/ul//li/div[1]/p[1]/text()[1] |/html/body/div[2]/div/div[2]/div[2]/ul//li/div[2]/h4/a/text()')
    for i in result:
        if i in dict:
            print(i)
