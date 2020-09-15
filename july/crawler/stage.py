# coding=utf-8
# 爬取stage帖子所有评论

import requests

from july.crawler import tool

requests.adapters.DEFAULT_RETRIES = 5
import importlib, sys;

importlib.reload(sys)

# 设定爬取页数
page = 1672

# 设定爬取帖子id
id = 1831320
for i in range(1, page):
    print(i)
    url = 'https://bbs.saraba1st.com/2b/thread-' + str(id) + '-' + str(i) + '-1.html'
    comment = tool.getTarget(url, '//td[@class="t_f"]/text()')
    for com in comment:
        if com != '\n' and com != '\r\n':
            tool.writetotxt('../data/stage/' + str(id) + '.txt', com[2:])
