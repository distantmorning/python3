import requests
import re
#凡爬虫,浏览器都无法直接打开
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）

url = 'https://matsuri.5ch.net/test/read.cgi/voiceactor/1561817994/'
dictAB = {}
pattern3 = re.compile('https://matsuri.5ch.net/test/read.cgi/voiceactor/(.*?)/', re.S)

for num in range(1,76):
    htmlA = requests.get(url=url, proxies=proxies)
    dictAB[num] = re.search(pattern3, htmlA.text)
    url = 'https://matsuri.5ch.net/test/read.cgi/voiceactor/' + dictAB[num] + '/'
    print(url)


