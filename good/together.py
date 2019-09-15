import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://zh.moegirl.org/zh-cn/" + "松冈祯丞", headers=headers)
s = requests.get("https://zh.moegirl.org/zh-cn/水濑祈", headers=headers)
pattern = re.compile('————《<a href=".*?" title=".*?">(.*?)</a>》', re.S)
pattern2 = re.compile('id="STAFF">STAFF.*?<ul><li>(.*?)</li>', re.S)
pattern3 = re.compile('音响监督(.*?)>', re.S)


def new_Page(url):
    n = requests.get(url, headers=headers)
    ttt = re.findall(pattern3, n.text)
    for rrr in ttt:
        print(rrr)


titles = re.findall(pattern, r.text)
title = re.findall(pattern, s.text)
dict = {}
for result in titles:
    for xxx in title:
        if result == xxx:
            dict[result] = 1
            # new_Page('https://zh.wikipedia.org/wiki/' + result)

# print(dict.keys())
for ld in dict.keys():
    print(ld)

print(len(dict))
