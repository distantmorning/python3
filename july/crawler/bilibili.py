# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import re
import os
import linecache
import sys
import time
import importlib,sys
import you_get
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
import requests
from bs4 import BeautifulSoup
import pandas as pd



#
# target = requests.get('https://www.bilibili.com/video/av78955967', headers=crawler.tool.getHeaders(), timeout=6)
# pattern = re.compile('cid=(.*?)&aid', re.S)
# cid = re.findall(pattern, target.text)
# comurl = 'http://comment.bilibili.com/' + cid[0] + '.xml'
#
# req = requests.get(comurl)
# html = req.content
# html_doc = str(html, 'utf-8')  # 修改成utf-8
#
# # 解析
# soup = BeautifulSoup(html_doc, "lxml")
#
# results = soup.find_all('d')
#
# contents = [x.text for x in results]
#
# for oc in contents:
#     crawler.tool.writetotxt('../test/shi.txt', oc)
# 保存结果
# table_dict = {"contents": contents}
# df = pd.DataFrame(table_dict)
# df.to_csv("bibi.txt", encoding='utf-8')


import sys
from you_get import common as you_get

# 读取txt文本内容
data = []
for line in open("url.txt", "r"):  # 设置文件对象并读取每一行文件
    data = data + line.splitlines()

# for 循环数组下载视频
for url in data:
    print(url)
    directory = r'F:\bilibili'  # 设置下载目录
    sys.argv = ['you-get','--playlist', '-o', directory, url]  # sys传递参数执行下载，就像在命令行一样
    you_get.main()
#you-get -i -s 127.0.0.1:59711 https://www.youtube.com/watch?v=pMxgov6_5TA

#you-get -x 127.0.0.1:59708 'https://www.youtube.com/watch?v=jNQXAC9IVRw'