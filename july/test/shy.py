# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import re
import os
import sys
import time
import importlib,sys
importlib.reload(sys)
headers = {'Connection': 'close',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

for i in range(130,200):
    link = 'https://qingbuyaohaixiu.com/?page=' + str(i)
    try :
        print('starting ' + str(i) + 'page')
        target = requests.get(link, headers=headers)
        html = etree.HTML(target.text)
        target.close()
        resurl = html.xpath('/html/body/div[2]//div//div/a[1]/@href')
        for j in resurl:
           newurl = 'https://qingbuyaohaixiu.com' + j
           sr = requests.get(newurl, headers=headers)
           html2 = etree.HTML(sr.text)
           rrr = html2.xpath('/html/body/div[2]/div[1]/div[1]/amp-img/@src')
           r = requests.get(rrr[0], headers=headers)
           fw = open('F:\shy\ '+ j[6:11] + '.jpg', 'wb')
           fw.write(r.content)
           r.close()
           sr.close()
           print('downloaded  ' + j[6:11])
    except :
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")
        continue