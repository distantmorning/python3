import requests
from bs4 import BeautifulSoup
import os
import re
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import logging
import linecache
import math
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
#创建下载目录
def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("f:\douban\d" + girlname, path))
    if not isExists:
        os.makedirs(os.path.join("f:\douban\d" + girlname, path))
        os.chdir(os.path.join("f:\douban\d" + girlname, path))
        return True
    else:
        return False

#进入豆瓣中某位演员的图片所在页面，选择按时间排序，经分析此时的链接，到下一页的时候，只有start的值增加了30，所以主要对start
#的值进行更改，对于不同的演员，更改URL，以及下面的最大页数就可以了，当然下载目录也可自行更改
url1 = 'https://movie.douban.com/celebrity/1274254/photos/?type=C&start='
url2 = '&sortby=time&size=a&subtype=a'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
girlname = 'zhangzifeng'
#30为相册的最大页数，埃文·蕾切尔·伍德 Evan Rachel Wood的图片最大页数为30

# image_list = []
# for i in (3,11,19,30):
#     i = 30*i
#     url = url1 + str(i) + url2
#     try:
#         target = requests.get(url, headers=headers)
#         #print('starting download ' + str(i))
#         mkdir(girlname + str(i))  # 创建文件名
#         html = etree.HTML(target.text)
#         target.close()
#         resurl = html.xpath('//*[@id="content"]/div/div[1]/ul//li/div[1]/a/@href')
#         # soup = BeautifulSoup(html.text, 'lxml')
#         # img_list = soup.find('ul', class_='poster-col3 clearfix').find_all('img')
#         for i in resurl:
#             image_list.append(i)
#     except:
#         print (i/30)
#
# for i in image_list:
#     with open('d2.txt', 'a', encoding='utf-8') as file:
#         file.write(i)
#         file.write('\n')
#
# 读取txt文本内容
data = []
for line in open("d1.txt", "r"):  # 设置文件对象并读取每一行文件
    data = data + line.splitlines()

url_list=[]
for i in data:
    try:
        target = requests.get(i, headers=headers)
        # html = etree.HTML(target.text)
        # target.close()
        # resurl = html.xpath('/html/body/div[3]/div[1]/div/div[1]/div[3]/span/a/@href')
        pattern3 = re.compile('celebrity.*img(.*?)doubanio.*jpg', re.S)
        resurl = re.findall(pattern3, target.text)
        for j in resurl:
            a = 'https://img' + resurl[0] + 'doubanio.com/view/photo/raw/public/p' + i[-10:-1] + '.jpg';
            print (a)
            url_list.append(j)
    except:
        with open('d2.txt', 'a', encoding='utf-8') as file:
            file.write(i)
            file.write('\n')

for i in url_list:
    with open('durl.txt', 'a', encoding='utf-8') as file:
        file.write(i)
        file.write('\n')


    # for i in img_list:
    #     img_s = i['src']
    #     name = img_s[-9:-4]
    #     img = requests.get(img_s)
    #     f = open(name + '.jpg', 'ab')
    #     f.write(img.content)
    #     f.close()