# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import lxml
import time
import os
import logging
import linecache
import re
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:59708',
    'https': 'https://' + '127.0.0.1:59708'
}

def downPhoto(link):
    try:
        r = requests.get(link, proxies=proxies, timeout=3)
        fw = open('F:\wenty\est2\ ' + link[-14:-5] + '.jpg', 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')




#循环某一类
pages = 47


def downPage(link2):
    target = requests.get(link2, timeout=50, proxies=proxies)
    html2 = etree.HTML(target.content)
    result3 = html2.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[4]/div/div/div[3]/div[1]/ol//li/ul/li[3]/text()')
    if len(result3) > 0:
        time.sleep(5)
        print(link2)


for i in range(40,pages ):  # 提取1到10页的内容
    print(i)
    link = 'http://gazounabi.com/archives/cat_6827.html?p=' + str(i)
    target = requests.get(link,timeout=50, proxies=proxies)
    html = etree.HTML(target.content)
    result2 = html.xpath('/html/body/div[2]/div[2]/div[1]/div/div/div[3]//div/div/div/div[1]/div[2]/h2/a/@href')
    for j in result2:
        downPage(j)





    # # #     downPhoto('https' + j + '.jpg')
    # link = 'http://gazounabi.com/archives/ayase_haruka_20140816.html'

    # for j in result3:
    #     print(j)
    #     #downPhoto(j)
    #
    #
    # # html = etree.HTML(content)
    # # resurl = html.xpath('//*[@id="main"]/div/div/div[3]/div[3]')
    # # print(len(resurl))
    # # for url in resurl:
    # #     #newtarget = requests.get('https://www.sex.com' + url, proxies=proxies)
    # #     with open('sexb.txt', 'a', encoding='utf-8') as file:
    # #         file.write(url + '\n')
