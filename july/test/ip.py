# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import os
import logging
import linecache
from retry import retry
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

# 获取代理ip池
def get_ip_list():
    contry=['wg','wp','np','ng']
    for nc in contry:
        urlip = 'http://www.iphai.com/free/'+nc
        html = requests.get(urlip, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip = tds[0].text[29:-24]
            port = tds[1].text[29:-24]
            try:
                requests.get('https://www.sex.com', proxies={'https': 'https://' + ip + ':' + port})
                print('https://' + ip + ':' + port + 'is useful!!!!!1')
                ip_list.append('https://' + ip + ':' + port)
            except:
                print('https://' + ip + ':' + port + '不可用')
    return ip_list


usefulip = []
usefulip = get_ip_list()
for uf in usefulip:
    with open('ip.txt', 'a', encoding='utf-8') as file:
        file.write(uf  + "\n")