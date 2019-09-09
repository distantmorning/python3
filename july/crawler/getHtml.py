import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
url = 'https://zh.moegirl.org/水濑祈'
html = requests.get(url, headers=headers)
# doc = pq(url= 'https://zh.moegirl.org/水濑祈',headers=headers)
print(html.text)
