import requests
from lxml import etree
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）

url = 'https://www.mau2.com/anime/kanatanoastra/casts'
target = requests.get(url,proxies=proxies,headers=headers)
print(target.text)


html = etree.HTML(target.text)
result = html.xpath('//*[@id="animeCasts"]/div[4]/table/tbody/tr[3]/td[2]/a/text()')




for i in result:
    url2 = 'https://www.mau2.com' + i
    html = etree.HTML(requests.get(url2, proxies=proxies,headers=headers).text)
    print(url2)
