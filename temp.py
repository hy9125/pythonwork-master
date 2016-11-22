# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
from pylab import * 

from scipy.cluster.vq import * 

list1 = [88.0,74.0,96.0,85.0]

list2 = [92.0,99.0,95.0,94.0]

list3 = [91.0,87.0,99.0,95.0]

list4 = [78.0,99.0,97.0,81.0]

list5 = [88.0,78.0,98.0,84.0]

list6 = [100.0,95.0,100.0,92.0]

data = vstack((list1,list2,list3,list4,list5,list6))

centroids,_ = kmeans(data,2)

result,_= vq(data,centroids)

print (result)
'''
'''tu
import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,4.,0.1)
plt.plot(t,t,t,t+2,t,t**t)
'''
'''
ad1=3
ad2=3
if ad1 == ad2:
    print( "the pass = %d"%(ad1*ad2))
'''
'''
k = int(input("shuru:"))
if k == 1:
    print("one")
elif k == 2:
    print("two")
else :
    print("else")
'''
'''
from random import randint

x= randint(0,300)
for count in range(0,5):
    print("cai")
    digit = int(input())
    
    if digit == x :
        print("bingo")
    elif digit> x :
        print("da,again")
    else :
        print("xiao,again")
'''
'''
f1 = open(r'e:\file.txt')
cnames = f1.readlines()
for i in range(0,len(cnames)):
    cnames[i]=str(i+1)+' '+cnames[i]
f1.close()
f2=open(r'e:\file2.txt','w')
f2.writelines(cnames)
f2.close()
'''

'''seek 
s = 'huzi huzi2 222 111'
f= open(r'e:\fileseek.txt','a+')
f.writelines('\n')
f.writelines(s)
f.seek(0,0)
cnames= f.readlines()
print(cnames)
f.close()
'''
'''
import numpy as np
#生成one
xArray = np.ones((3,4))
xArray
Out[7]: 
array([[ 1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.],
       [ 1.,  1.,  1.,  1.]])
'''
'''
线性代数
from scipy import linalg
arr= np.array([[1,2],[3,4]])

linalg.det(arr)
Out[11]: -2.0

'''
'''财经雅虎
from matplotlib.finance import quotes_historical_yahoo_ochl

from datetime import date

import pandas as pd

today = date.today()

start = (today.year-1,today.month,today.day)

quotes = quotes_historical_yahoo_ochl('AXP',start,today)

fields=['date','open','close','high','low','volume']
df = pd.DataFrame(quotes,columns=fields)
print (df)
'''
'''日期函数
from datetime import date
firstday =date.fromordinal(735190)
'''
'''转换
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 
today = date.today()

start = (today.year-1,today.month,today.day)

quotes = quotes_historical_yahoo_ochl('AXP',start,today)

fields=['date','open','close','high','low','volume']
list1 =[]
for i in range(0,len(quotes)):
    #转换成常规时间
    x=date.fromordinal(int(quotes[i][0]))
    #转换成固定格式
    y=datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf=pd.DataFrame(quotes,index=list1,columns=fields)
quotesdf=quotesdf.drop(['date'],axis=1)
print(quotesdf)
'''
'''
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd 
today = date.today()

start = (today.year-1,today.month,today.day)

quotes = quotes_historical_yahoo_ochl('AXP',start,today)

fields=['date','open','close','high','low','volume']
listtemp =[]
for i in range(0,len(quotes)):
    temp= time.strptime(quotesdf.insex)
'''
'''k-means
from pylab import *
from scipy.cluster.vq import *
list1=[88,74,96,85]
list2=[92,99,95,94]
list3=[91,87,99,95]
list4=[78,99,97,81]
list5=[88,78,98,84]
list6=[100,95,100,92]
data=vstack((list1,list2,list3,list4,list5,list6))
centroids,_ =kmeans(data,2)
result,_=vq(data,centroids)
print(result)
'''
'''图
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y)
'''
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y,'r--')
plt.title('frist')
plt.show()
'''
'''绘制在同一个途中
#data is ready
#211表示两行一列
subplot(211)
plt.plot(listKOIndex,listKO,color='r',marker='o')
subplot(212)
plt.plot(listKOIndex,listKO,color='green',marker='o')
#axes([left,bottom,width,height])
'''
'''excal读取
import pandas as pd
stu_df = pd.DataFrame()
stu_df = pd.read_excel('d:\\stu_scores.xlsx', sheet_name = 'scores')
stu_df['sum'] = stu_df['Python'] + stu_df['Math']
stu_df.to_excel('d:\\stu_scores.xlsx', sheet_name = 'scores')
'''
'''
import time
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import  datetime
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
start = datetime(2015,1,1) 
end = datetime(2015,12,31) 
quotesMSFT = quotes_historical_yahoo_ochl('MSFT',start,end)
quotesINTC = quotes_historical_yahoo_ochl('INTC',start,end)
fields=['date','open','close','high','low','volume']
list1=[]
for i in range(0,len(quotesMSFT)):
    #dromordinal 将格式转化为date
    x = date.fromordinal(int(quotesMSFT[i][0]))
    #转化为指定格式
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
list2=[]
for i in range(0,len(quotesINTC)):
    x = date.fromordinal(int(quotesINTC[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list2.append(y)
quotesmsftdf = pd.DataFrame(quotesMSFT,index=list1,columns=fields)
#去掉原来的DATE
quotesmsftdf = quotesmsftdf.drop(['date'],axis=1)
#print(quotesmsftdf) 
quotesintcdf = pd.DataFrame(quotesINTC,index=list1,columns=fields)
quotesintcdf = quotesintcdf.drop(['date'],axis=1)
listtemp1 = []
for i in range(0,len(quotesmsftdf)):
    temp = time.strptime(quotesmsftdf.index[i],"%Y-%m-%d")
    #只统计月
    listtemp1.append(temp.tm_mon)
listtemp2 = []
for i in range(0,len(quotesintcdf)):
    temp = time.strptime(quotesintcdf.index[i],"%Y-%m-%d")
    listtemp2.append(temp.tm_mon)

tempmsftdf= quotesmsftdf.copy()
tempmsftdf['month']=listtemp1
closemaxMSFT=tempmsftdf.groupby('month').max().close
listMSFT=[]
for i in range(1,13):
    listMSFT.append(closemaxMSFT[i])
listMSFTIndex=closemaxMSFT.index
tempintcdf = quotesintcdf.copy()
tempintcdf['month']= listtemp2
closemaxINTC=tempintcdf.groupby('month').max().close
listINTC=[]
for i in range(1,13):
    listINTC.append(closemaxINTC[i])
listINTCIndex=closemaxINTC.index
pl.subplot(211)
plt.plot(listMSFTIndex,listMSFT,color='r',marker='o')
pl.subplot(212)
plt.plot(listINTCIndex,listINTC,color='green',marker='o')
plt.show()
'''
'''python2.7
import wx 
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self, parent = superior, title = "Hello World in wxPython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1= wx.TextCtrl(panel, value = "Hello, World!", size = (200,180), style = wx.TE_MULTILINE)
        sizer.Add(self.text1, 0, wx.ALIGN_TOP | wx.EXPAND)
        button = wx.Button(panel, label = "Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)        
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self, text):
        self.text1.AppendText("\nHello, World!")
if __name__ == '__main__': 
    app =wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
'''

