# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 09:23:35 2016

@author: 70479
"""
import pandas as pd

catering_sale = 'D:/fenxi/chapter3/demo/data/catering_sale.xls'
data = pd.read_excel(catering_sale,index_col=u'日期')
#读取日期，以“日期”为索引

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

plt.figure()#建立图像
p = data.boxplot()
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()

#用annotate添加注释
#其中有些相近的点，注解会出现重叠，难以看清，需要一些技巧来控制。
#以下参数都是经过调试的，需要具体问题具体调试。
#xy表示要标注的位置坐标，xytext表示文本所在位置
for i in range(len(x)): 
  if i>0:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
  else:
    plt.annotate(y[i], xy = (x[i],y[i]), xytext=(x[i]+0.08,y[i]))
plt.show() #展示箱线图

                     
