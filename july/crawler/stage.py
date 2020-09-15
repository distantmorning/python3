# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests

from july import crawler

requests.adapters.DEFAULT_RETRIES = 5
import os.path
import re
import os
import linecache
import sys
import time
import importlib,sys;
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)

def getTarget(link,xpathx):
    resurl = []
    try:
        target = requests.get(link, timeout=6)#,proxies=getProxies()
        html = etree.HTML(target.text)
        target.close()
        resurl = html.xpath(xpathx)
        return resurl
    except:
        return resurl

def writetotxt(filename,str):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str)
        file.write('\n')

for i in range(110,1672):
    print(i)
    url = 'https://bbs.saraba1st.com/2b/thread-1831320-' + str(i) +'-1.html'
    comment = getTarget(url,'//td[@class="t_f"]/text()')
    for com in comment:
        if com != '\n' and com != '\r\n':
           writetotxt('../data/sta.txt', com[2:])