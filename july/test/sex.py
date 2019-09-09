# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
import os.path
import re
import os
import sys
import time
import importlib,sys
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}

def geturls(target):
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="masonry_container"]//div/a/img/@data-src')
    for url in resurl:
        r = requests.get(url.replace('/300/','/620/'))
        if url.endswith('gif'):
            path = 'F:\sex\gif\ '+ url[53:61] + '.gif'
        else:
            path = 'F:\sex\pic\ '+ url[53:61] + '.jpg'
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
#https://www.sex.com/user/dplayer/likes/?page='
#'https://www.sex.com/?sort=popular&sub=all&page='
#'https://www.sex.com/pics/?sort=popular&sub=all&page='
if __name__ == '__main__':
    pool = ThreadPool(4) #双核电脑
    tot_page = []
    for i in range(1,3): #提取1到10页的内容
        link = 'https://www.sex.com/gifs/?sort=popular&sub=all&page=' + str(i)
        tot_page.append(link)
    pool.map(spider, tot_page)#多线程工作
    pool.close()
    pool.join()
