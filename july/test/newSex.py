# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import os
import logging
import linecache
import re
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}


def geturls(target):
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="masonry_container"]//div/a/img/@data-src')
    for url in resurl:
        r = requests.get(url.replace('/300/', '/620/'))
        if url.endswith('gif'):
            path = 'F:\sex\gif\ ' + url[53:61] + '.gif'
        else:
            path = 'F:\sex\pic\ ' + url[53:61] + '.jpg'
        if os.path.exists(path):
            continue
        fw = open(path, 'wb')
        print('downloading:' + path)
        fw.write(r.content)
    print('down')


def spider(url):
    print(url)
    print('当前执行URL:' + url)
    html = requests.get(url, proxies=proxies)
    geturls(html)
    print('当前执行URL:' + url + '已完成')



for i in range(1, 66):  # 提取1到10页的内容
    link = 'https://www.sex.com/pics/blowjob/?sort=popular&sub=all&page=' + str(i)
    target = requests.get(link,timeout=5)#, proxies=proxies)
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="masonry_container"]//div/a[@class="image_wrapper"]/@href')
    for url in resurl:
        #newtarget = requests.get('https://www.sex.com' + url, proxies=proxies)
        with open('sexb.txt', 'a', encoding='utf-8') as file:
            file.write(url + '\n')



