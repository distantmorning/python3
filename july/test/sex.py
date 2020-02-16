# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import logging
import random
import linecache
import os.path
import re
import os
import sys
import time
from retry import retry
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}


def getListFromPath(pathroute):
    strLine = []
    ipstr = linecache.getlines(pathroute)
    for ip in ipstr:
        strLine.append(ip[0:-1])
    return strLine




def get_random_ip():
    proxy_ip = random.choice(ip_list)
    proxies = {'https': proxy_ip}
    return proxies

def geturls(target):
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="masonry_container"]//div/a/img/@data-src | //*[@id="masonry_container"]/div/a/@href')
    for i in range(0,len(resurl)):
        if i % 2 ==0:
            baseUrl = resurl[i+1].replace('/300/','/620/')
            ttt = requests.get('https://www.sex.com' + resurl[i],proxies = proxies)
            html2 = etree.HTML(ttt.text)
            title = html2.xpath('/html/head/title')
            newUrl = baseUrl

def spider(url):
    print(url)
    print('当前执行URL:' + url)
    html = requests.get(url, proxies=proxies)
    geturls(html)
    print('当前执行URL:' + url + '已完成')
#https://www.sex.com/user/dplayer/likes/?page='
#'https://www.sex.com/?sort=popular&sub=all&page='
#'https://www.sex.com/pics/?sort=popular&sub=all&page='



cat = ['creampie','celebrity','hardcore','blowjob','girlfriend','teen','amateur','college','cumshots',]


def getUU(link):
    for i in range(1, 30):  # 提取1到10页的内容
        #link = 'https://www.sex.com/gifs/' + c + '/?sort=popular&sub=all&page=' + str(i)
        print(link)
        try:
            getName(link)
        except:
            print('error is happenning!!!!!!1')


def getName(link):
    target = requests.get(link,timeout=10)  # , proxies=proxies)
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="masonry_container"]//div/a[@class="image_wrapper"]/@href')
    trel = html.xpath('//*[@id="masonry_container"]//div/div[1]/a//text()')
    for tn in range(0, len(resurl)):
        # repines      likes          comments
        if int(trel[tn * 3]) > 300 and int(trel[tn * 3 + 1]) > 300 and int(trel[tn * 3 + 2]) > 4:
            with open('sexall.txt', 'a', encoding='utf-8') as file:
                file.write(resurl[tn] + '\n')


# for i in range(1,30):
#     newLink = 'https://www.sex.com/videos/?sort=popular&sub=all&page=' + str(i)
#     try:
#         getName(newLink)
#     except:
#         print(newLink + 'error')
#
#






# for c in cat:
#     getUU()
#


#
# dictD = []
# for file in os.listdir('F:\sex'):
#     dictD.append('/pin/' + file[1:-4] + '/\n')
#
#
#
#
#
#
#
# urls = []
# au = linecache.getlines('sexall.txt')
# for a in au:
#     if a not in dictD:
#         urls.append(a[0:-1])
#
# @retry(tries=5,delay=2)
# def downPhoto(i,testurl,headers):
#     target = requests.get(testurl,headers=headers,timeout=3)#,proxies=get_random_ip())
#     html = etree.HTML(target.text)
#     turl = html.xpath('//*[@class="image_frame"]//img/@src')
#     print(turl)
#     r = requests.get(turl[0], headers=headers, timeout=3)#,proxies=get_random_ip())
#     return r
#
#
#
# def spider2(i):
#     testurl = 'https://www.sex.com' + i
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
#     'Referer':'https://www.sex.com' + i}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
#     try:
#         r = downPhoto(i,testurl,headers)
#         fw = open('F:\sex\ ' + i.split("/")[-2] + '.gif', 'wb')
#         fw.write(r.content)
#         r.close()
#     except:
#         print(testurl)
#
#
#
# pool = ThreadPool(10)  # 双核电脑
# pool.map(spider2, urls)  # 多线程工作
# pool.close()
# pool.join()


videoLine = getListFromPath('sexall.txt')


def work():
    target = requests.get('https://www.sex.com' + url, timeout=5)
    tt = re.findall('\'\/video\/stream\/(.*?)\',', target.text)
    print(tt[0])
    newhtml = requests.post('https://www.sex.com/video/stream/' + tt[0], allow_redirects=False, timeout=5)
    print(newhtml.headers['location'])
    with open('xunlei.txt', 'a', encoding='utf-8') as file:
        file.write(newhtml.headers['location'] + '\n')


for url in videoLine:
    print(url)
    try:
        work()
    except:
        print('error')
# html = requests.post('https://www.sex.com/video/stream/868281', allow_redirects=False)
# # print(html.headers['location'])










