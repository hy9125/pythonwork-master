# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:16:35 2016

@author: 70479
"""

# -*- coding: utf-8 -*-
 
from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import numpy
import scipy.stats
import matplotlib.pyplot as plt
  
def _wxdate2pydate(date):
     import datetime
     if date.IsValid():
          ymd = map(int, date.FormatISODate().split('-'))
          return datetime.date(*ymd)
     else:
          return None
  
def PlotData(code, start, end, list):
    start_date = _wxdate2pydate(start)
    end_date = _wxdate2pydate(end)
    print (code)
    print (start_date)
    print (end_date)
    quotes = quotes_historical_yahoo_ochl(code, start_date, end_date)
    fields = ['date','open','close','high','low','volume']
    list1 = []
    for i in range(0,len(quotes)):
        x = date.fromordinal(int(quotes[i][0]))
        y = datetime.strftime(x,'%Y-%m-%d')
        list1.append(y)
    print (list1)
      
    quotesdf = pd.DataFrame(quotes, index = list1, columns = fields)
    quotesdf = quotesdf.drop(['date'], axis = 1)
    quotesdftemp = pd.DataFrame()
   
    for i in range(0,len(list)):
        quotesdftemp[list[i]] = quotesdf[list[i]]
     
    print (quotesdftemp)
    print ("ready to plot")
    quotesdftemp.plot()
    plt.show()