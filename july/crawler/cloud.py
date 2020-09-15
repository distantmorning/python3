from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
from os import path
import jieba
#根据文本文件生成云图


#待生成文本路径
txtpath= '../data/flag.txt'

#设置背景图片
backimage = '../data/qi.jpg'

#设置保存路径
savepath = '../data/flagall.png'

lj=path.dirname(__file__)   #当前文件路径
text=open(path.join(lj,txtpath),encoding='utf-8').read() #读取的文本
# jieba.add_word('小水')
# jieba.add_word('松冈')    #添加结巴分辨不了的词汇
jbText=' '.join(jieba.cut(text))



imgMask=np.array(Image.open(path.join(lj, backimage)))   #读入背景图片
wc=WordCloud(
    background_color='white',
    max_words=500,
    font_path='msyh.ttc',    #默认不支持中文
    mask=imgMask,  #设置背景图片
    random_state=30 #生成多少种配色方案
).generate(jbText)

ImageColorGenerator(imgMask)   #根据图片生成词云颜色
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
wc.to_file(path.join(lj, savepath))
print('成功保存词云图片！')


