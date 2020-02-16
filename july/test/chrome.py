from selenium import webdriver

def getAnimeName(name):
    browser = webdriver.Chrome()
    dictAB = []
    browser.get('https://www.mau2.com/voice/' + name)
    inputs = browser.find_elements_by_xpath('/html/body/div[3]/div[5]/dl//dd/dl//dt/span[2]/a')
    for i in range(0, len(inputs)):
        dictAB.append(inputs[i].get_attribute('href'))
    browser.close()
    return  dictAB


inori = getAnimeName('c613e9')
tgtg = getAnimeName('5f3dce')


def getNum(name):
    browser = webdriver.Chrome()
    browser.get(j + '/casts?q=' + name)
    inputs = browser.find_elements_by_xpath('//*[@id="animeCasts"]//div/table/tbody/tr[1]/th/a')
    dic = []
    for i in range(0, len(inputs)):
        dic.append(inputs[i].get_attribute('text'))
    browser.close()
    return (dic)


for j in inori:
    for k in tgtg:
        if j == k:
            print(j)
            c1 = getNum('水瀬いのり')
            c2 = getNum('松岡禎丞')
            for u in c1:
                for v in c2:
                    if u == v:
                        print(u)