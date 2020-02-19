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
import crawler.tool
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)

for i in range(110,1672):
    print(i)
    url = 'https://bbs.saraba1st.com/2b/thread-1831320-' + str(i) +'-1.html'
    comment = crawler.tool.getTarget(url,'//td[@class="t_f"]/text()')
    for com in comment:
        if com != '\n' and com != '\r\n':
           crawler.tool.writetotxt('../test/sta.txt', com[2:])