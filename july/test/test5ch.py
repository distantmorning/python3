# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import logging
import linecache
import re
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:61614',
    'https': 'https://' + '127.0.0.1:61614'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101Firefox/38.0'}


def getUrl():
    baseUrl = 'http://find.2ch.sc/index.php?STR=%C6%E2%C5%C4%BF%BF%CE%E9&SCEND=D&SORT=NPOSTS&COUNT=50&TYPE=TITLE&BBS=ALL&OFFSET='
    dictAB = {}
    pattern3 = re.compile('https(.*?).jpg', re.S)
    for num in range(1, 20):
        newnum = num * 50 - 50
        newUrl = baseUrl + str(newnum)
        target = requests.get(url=newUrl, proxies=proxies)
        html = etree.HTML(target.text)
        target.close()
        result = html.xpath('/html/body/div[2]/div/nbsp/dl//dt/a/@href')
        for i in result:
            target1 = requests.get(url=i, proxies=proxies).text
            result2 = re.findall('https(.*?).jpg', target1)
            for j in result2:
                with open('photo.txt', 'a', encoding='utf-8') as file:
                    file.write('https' + j + '.jpg' + '\n')


def downPhoto(link):
    try:
        r = requests.get(link[:-1], proxies=proxies, timeout=3)
        fw = open('F:\ch\single\ ' + link[-12:-5] + '.jpg', 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')




def getSUrl():
    baseUrl = 'http://ikura.2ch.sc/test/read.cgi/voiceactor/1460324821/0-'
    target1 = requests.get(baseUrl, proxies=proxies).text
    result2 = re.findall('https(.*?).jpg', target1)
    for j in result2:
        downPhoto('https' + j + '.jpg')



getSUrl()

# pool = ThreadPool(10) #双核电脑
# tot_page = []
# str = linecache.getlines('photo2.txt')
# pool.map(downPhoto, str)  # 多线程工作
# pool.close()
# pool.join()