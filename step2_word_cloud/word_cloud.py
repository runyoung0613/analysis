
import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  
from wordcloud import WordCloud,ImageColorGenerator
import os
#import matplotlib.mlab as mlab    

font = FontProperties(fname='Songti.ttc')  
bar_width = 0.5
lyric= ''

f=open('e:/analysis/step1_cut_words/temp data/contents_keywords.dat','r', encoding='utf-8')

for i in f:
    lyric+=f.read()
# print(lyric)#自动加+'\n'

# 考虑了相邻词的语义关系、基于图排序的关键词提取算法TextRank
result=jieba.analyse.textrank(lyric,topK=50,withWeight=True)

keywords = dict()
for i in result:
    keywords[i[0]]=i[1]
print(keywords)

image= Image.open('e:/analysis/step2_word_cloud/background1.png')
graph = np.array(image)
print(graph)
wc = WordCloud(font_path='C:/Windows/Fonts/simhei.ttf',background_color='White',max_words=50,mask=graph)
wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)#设置背景图像
plt.imshow(wc)  #画图
plt.imshow(wc.recolor(color_func=image_color))  #根据背景图片着色
plt.axis("off") #不显示坐标轴
plt.show()

# 保存到固定路径，每次运行覆盖原文件
output_path = 'e:/analysis/step2_word_cloud/output.png'
print(f'保存词云图像到: {output_path}')
wc.to_file(output_path)

# X=[]  
# Y=[] 

# for key in keywords:
    
#     X.append(key)
#     Y.append(keywords[key])

# num = len(X)
   
# fig = plt.figure(figsize=(28,10))  #图的高宽
# plt.bar(range(num),Y,tick_label = X,width = bar_width)
# #plt.xlabel("X-axis",fontproperties=font)  
# #plt.ylabel("Y-axis",fontproperties=font)
# plt.xticks(rotation = 50,fontproperties=font,fontsize=20)
# plt.yticks(fontsize=20)
# plt.title("words-frequency chart",fontproperties=font,fontsize=30)  
# plt.savefig("barChart.jpg",dpi = 360)
# plt.show()