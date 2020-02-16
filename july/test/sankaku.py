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
    #urlip = 'http://www.xicidaili.com/nn/'
    urlip = 'http://www.iphai.com/free/wg'
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
            requests.get('https://chan.sankakucomplex.com', proxies={'https': 'https://' + ip + ':' + port})
            print('https://' + ip + ':' + port + 'is useful!!!!!1')
            ip_list.append(ip + ':' + port)
        except:
            print('https://' + ip + ':' + port + '不可用')
    return ip_list


# 从ip代理池随机选取一个ip返回
def get_random_ip():
    proxy_ip = random.choice(ip_list)
    proxies = {'https': proxy_ip}
    return proxies

proxies = {
    #'http': 'http://' + '127.0.0.1:61614',
    'http': 'http://112.87.69.44:9999',
    'https':'https://112.87.69.44:9999'
    #'https': 'https://' + '127.0.0.1:61614'
    #'http': get_random_ip()
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





def getPageUrl(url):
    try:
        html = requests.get(url[0:-1], headers=headers,timeout=10)
        target = etree.HTML(html.text)
        result = target.xpath('//div[@class = "content"]//span/a/@href')
        for newUrl in result:
            with open('allurl.txt', 'a', encoding='utf-8') as file:
                file.write('https://chan.sankakucomplex.com' + newUrl + '\n')
        with open('page.txt', 'a', encoding='utf-8') as file:
            file.write(url + '\n')
    except:
        logging.warning(url + 'didnt get the html!!!!!1')
        with open('errorurl.txt', 'a', encoding='utf-8') as file:
            file.write(url)



def newSpider(url):
    xpathstr = '//*[@id="image-link"]/img/@src'
    r = gerContent(url,xpathstr)
    path = 'F:\sankaku\ ' + url[0:-1].split('/')[-1] + '.jpg'
    fw = open(path, 'wb')
    fw.write(r.content)
    print('downloaded' + url[0:-1])





# def newSpider(url):
#     try:
#         r = gerContent(url)
#         path = 'F:\sankaku\ ' + url[0:-1].split('/')[-1] + '.jpg'
#         fw = open(path, 'wb')
#         fw.write(r.content)
#         print('downloaded' + url[0:-1])
#     except:
#         time.sleep(10)
#         print('stop 5 sec , error when downloading' + url[0:-1])
#





@retry()
def gerContent(url,xpathstr):
    iport = get_random_ip()
    html = requests.get(url[0:-1], headers=headers, timeout=10,proxies=iport)
    # time.sleep(3)
    target = etree.HTML(html.text)
    result = target.xpath(xpathstr)
    r = requests.get('https:' + result[0], headers=headers, timeout=10,proxies=iport)
    return r


def videoSpider(url):
    try:
        vxpath = '//*[@id="image"]/@src'
        r = gerContent(url,vxpath)
        path = 'F:\sankaku\ ' + url[0:-1].split('/')[-1] + '.mp4'
        fw = open(path, 'wb')
        fw.write(r.content)
        print('downloaded' + url[0:-1])
    except:
        time.sleep(10)
        print('stop 5 sec , error when downloading' + url[0:-1])

ip_list = []
ipstr = linecache.getlines('ip.txt')
for ip in ipstr:
    ip_list.append(ip[0:-1])

for f in range(1,100):
    urlLine = linecache.getlines('urls.txt')
    dictD = []
    for file in os.listdir('F:\sankaku'):
        dictD.append(file[1:-4])
    print('get all downloaded jpg' + str(len(dictD)))
    pool = ThreadPool(10)  # 双核电脑
    tot_page = []
    for i in urlLine:
        numP = i[0:-1].split('/')[-1]
        if numP not in dictD:
            tot_page.append(i)
    print('get all need downloading jpg url' + str(len(tot_page)))
    pool.map(newSpider, tot_page)  # 多线程工作
    pool.close()
    pool.join()
    time.sleep(60)


