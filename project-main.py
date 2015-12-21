# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 15:58:33 2015

@author: xiaoqin
"""

#from matplotlib.finance import quotes_historical_yahoo_ochl
#from datetime import date
#import pandas as pd
#today = date.today()
#start = (today.year-1, today.month, today.day)
#quotes =  quotes_historical_yahoo_ochl('AXP',start,today)
#df = pd.DataFrame(quotes)
#print df.head()

import pandas as pd
from pandas.io.data import DataReader

symbols_list = [ 'SPY']#, 'AAPL', 'GLD', 'XOM']#'ORCL', 'TSLA']#, 'IBM','YELP', 'MSFT']
d = {}
for ticker in symbols_list:
    d[ticker] = DataReader(ticker, "yahoo", '2014-12-01')
pan = pd.Panel(d)
df1 = pan.minor_xs('Adj Close')
print(df1)
df1.plot()
df1.to_csv('spy.csv', sep='\t')