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


pageurl = crawler.tool.getVPNTarget('https://sp.nicovideo.jp/watch/sm36342881','//*[@id="jsCommentListContainer"]/div/div[2]/div[1]/div/div/div[5]/div[1]/text()')
print(pageurl[0])