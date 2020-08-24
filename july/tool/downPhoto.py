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
import logging
import linecache
import re
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:1080',
    'https': 'https://' + '127.0.0.1:1080'
}


def downPhoto(filename , link):
    try:
        r = requests.get(link[:-1], headers=headers, timeout=15,proxies=proxies)
        fw = open('F:\pic\ch\sg\ ' + filename, 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')

def downPhotos(sss):
    filename = sss.split("   ")[0];
    link = sss.split("   ")[1];
    try:
        r = requests.get(link[:-1], headers=headers, timeout=15,proxies=proxies)
        fw = open('F:\pic\ch\sg\ ' + filename, 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')


# r = requests.get('https://i.imgur.com/zvw8NZC.png', headers=headers, timeout=3,proxies=proxies)
# fw = open('test.jpg', 'wb')
# fw.write(r.content)
# r.close()

str = linecache.getlines('tgtgt3.txt')
pool = ThreadPool(50) #双核电脑
tot_page = []
# for sss in str:
#     downPhoto(sss.split("   ")[0],sss.split("   ")[1])
#     print(sss.split("   ")[0])
for sss in str:
    tot_page.append(sss)
pool.map(downPhotos, tot_page)#多线程工作
pool.close()
pool.join()
