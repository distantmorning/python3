# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import logging
import linecache
import os.path
import re
import os
import sys
import time
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
headers = {'Connection': 'close',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

def getTitle(link):
    target = requests.get(link, headers=headers, timeout=10)
    html = etree.HTML(target.text)
    target.close()
    resurl = html.xpath('//article/header/h2/a/@href')
    for i in resurl:
        newlink = 'http://www.mingtuiw.com'+ i
        try:
            getPage(newlink)
        except:
            logging.debug('PageError' + link)
def getPage(link):
    target = requests.get(link, headers=headers, timeout=10)
    html = etree.HTML(target.text)
    target.close()
    resurl = html.xpath('//article/div//p//a/@href')
    for i in resurl:
        newlink = 'http://www.mingtuiw.com'+ i
        try:
            getUrl(newlink)
        except:
            logging.debug('UrlError' + link)
def getUrl(link):
    target = requests.get(link, headers=headers, timeout=10)
    html = etree.HTML(target.text)
    target.close()
    resurl = html.xpath('//article/div/div/div[1]/a/img/@src')
    if len(resurl) > 0:
        with open('赵丽颖.txt', 'a', encoding='utf-8') as file:
            file.write('http://www.mingtuiw.com'+resurl[0])
            file.write('\n')


def getList():
    for i in range(1, 20):
        link = 'http://www.mingtuiw.com/archives/category/演员/迪丽热巴/page/' + str(i)
        try:
            getTitle(link)
        except:
            logging.debug('TitleError' + link)

def downPhoto(link):
    try:
        r = requests.get(link[:-1], headers=headers, timeout=3)
        fw = open('F:\leg\dlrb\ ' + link[51:-13] + '.jpg', 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')


pool = ThreadPool(4) #双核电脑
tot_page = []
str = linecache.getlines('porn2.txt')
pool.map(downPhoto, str)  # 多线程工作
pool.map(getTitle,tot_page)
pool.close()
pool.join()