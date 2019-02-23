#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__: 陌路疏途


# 四部曲：1.导入模块 2.获取网页源码 3.正则匹配下载 4.调用函数

import urllib.request #获取网址模块
import re  #正则匹配模块

#定义获取网页源代码函数
def gethtml():
    papg = urllib.request.urlopen('http://www.wmpic.me/tupian/cute') #打开图片的网址
    html = papg.read()  #用read方法读成网页源代码，格式为字节对象
    html = html.decode('UTF-8') #定义编码格式解码字符串(字节转换为字符串)
    return html

#匹配

def getimg(html):
    imgre = re.compile(r' src="(.*?)" class=')#正则匹配，compile为把正则表达式编译成一个正则表达式对象，提供效率。
    imglist = re.findall(imgre, html)#获取字符串中所有匹配的字符串
    x = 0 #定义全局变量默认为0
    for imgurl in imglist: #循环图片字符串列表并输出
        print(imgurl)

#下载
        urllib.request.urlretrieve(imgurl,'D:\\pictures\%s.jpg' % x)#把图片下载到本地并指定保存目录
        x += 1 #每次自增1
        print("正在下载第%s张" % x)#格式化输出张数

#调用函数
html = gethtml()

print(getimg(html))