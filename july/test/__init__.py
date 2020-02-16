# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import os
import logging
import linecache
import re
from selenium import webdriver
import time
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
import random
from bs4 import BeautifulSoup
headers = {'Connection': 'close',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

# urlLine = linecache.getlines('allurl.txt')
# dictD = []
# for i in urlLine:
#     if len(i) >2 :
#         dictD.append(i[0:-1])
#
# newD = []
# for i in dictD:
#     if i not in newD:
#         newD.append(i)
#
# for j in newD:
#     with open('urls.txt', 'a', encoding='utf-8') as file:
#         file.write(j + '\n')
#





# clock = []
# for y in range(2007,2020):
#     for m in range(1,13):
#         clock.append(str(y) + '-' + str(m) + '-01')
#
# seqs = []
# for i in range(0,len(clock)-1):
#     seqs.append(clock[i] + '..' + clock[i+1])
#
#
# for seq in seqs:
#     for n in range(1,16):
#         url = 'https://chan.sankakucomplex.com/?tags=fav%3Aielgnid%20date%3A' + seq + '&page='+  str(n)
#         if url in dictD:
#             continue
#         try:
#             html = requests.get(url, headers=headers, timeout=10)
#         except requests.exceptions.ConnectionError:
#             print(url)
#             continue
#         target = etree.HTML(html.text)
#         result = target.xpath('//div[@class="content"]//span/a')
#         if (len(result)) > 0:
#             with open('pageurl.txt', 'a', encoding='utf-8') as file:
#                 file.write(url + '\n')
#         else:
#             break

# def getPageUrl(url):
#     try:
#         html = requests.get(url[0:-1], headers=headers,timeout=10)
#         target = etree.HTML(html.text)
#         result = target.xpath('//div[@class = "content"]//span/a/@href')
#         if len(result) < 20 :
#             logging.warning(url + 'has problem!!!!!!')
#         for newUrl in result:
#             with open('allurl.txt', 'a', encoding='utf-8') as file:
#                 file.write('https://chan.sankakucomplex.com' + newUrl)
#                 file.write('\n')
#         logging.warning(url[0:-1] + 'is right')
#     except:
#         logging.warning(url + 'didnt get the html!!!!!1')
#         with open('url3.txt', 'a', encoding='utf-8') as file:
#             file.write(url)
#

html = requests.post('https://www.sex.com/video/stream/868281', allow_redirects=False)
print(html.headers['location'])