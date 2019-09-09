# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import logging
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)
import re
import os
from multiprocessing.dummy import Pool as ThreadPool
import sys
import time
import importlib,sys
importlib.reload(sys)
headers = {'Connection': 'close',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


def spider(link):
    try:
        work(link)
    except:
        time.sleep(5)
        logging.info('stop for rest 5 sec')

def work(link):
    target = requests.get(link, headers=headers, timeout=3)
    html = etree.HTML(target.text)
    target.close()
    resurl = html.xpath('/html/body/div[2]/div[1]/div[1]/amp-img/@src')
    if len(resurl) > 0:
        r = requests.get(resurl[0], headers=headers, timeout=3)
        fw = open('F:\shy\ ' + link[-4:] + '.jpg', 'wb')
        fw.write(r.content)
        r.close()
        logging.info('downloaded  ' + link[-4:])
    else:
        logging.info(link[-4:])


pool = ThreadPool(4) #双核电脑
tot_page = []
for i in range(4968, 9895):
    link = 'https://qingbuyaohaixiu.com/post/' + str(i)
    tot_page.append(link)
pool.map(spider, tot_page)  # 多线程工作
pool.close()
pool.join()