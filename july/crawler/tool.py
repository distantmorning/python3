import requests
from lxml import etree
proxies = {
    'http': 'http://' + '127.0.0.1:59708',
    'https': 'https://' + '127.0.0.1:59708'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def getProxies():
    return proxies

def getHeaders():
    return headers

def ppp():
    print('hello,ddd')


#图片url,图片路径，图片名称
def downPhoto(url,path,name):
    r = requests.get(url, headers=getHeaders(), timeout=15)
    fw = open(path + name + '.jpg', 'wb')
    fw.write(r.content)
    r.close()
    fw.close()
    print('downloaded  ' + name)

#页面url，开始，结束
def getAllPages(url,j,k):
    links = []
    for i in range(j,k):
        link = url + str(i)
        links.append(link)
    return links


#获取页面中特定的path属性
#url,path
def getTarget(link,xpathx):
    resurl = []
    try:
        target = requests.get(link, headers=getHeaders(), timeout=6)#,proxies=getProxies()
        html = etree.HTML(target.text)
        target.close()
        resurl = html.xpath(xpathx)
        return resurl
    except:
        return resurl


def getVPNTarget(link,xpathx):
    resurl = []
    try:
        target = requests.get(link, headers=getHeaders(), proxies=getProxies(),timeout=6)#,
        html = etree.HTML(target.text)
        target.close()
        resurl = html.xpath(xpathx)
        return resurl
    except:
        return resurl






def writetotxt(filename,str):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str)
        file.write('\n')