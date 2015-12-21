# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:55:49 2015

@author: xiaoqin
"""

import pandas as pd
import re
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.optimize as spo

def assess_portfolio(df):
    #print allocation,starting_amount
    daily_ret = df.copy()
    daily_ret[1:]=(df[1:]/df[:-1].values)-1
    daily_ret.ix[0,:]=0
    #daily_ret = daily_ret*allocation
    cum_ret = df.copy()
    cum_ret[1:]=(df[1:].values/df[0:1].values)-1
    cum_ret.ix[0,:]=0
    #cum_ret = cum_ret*allocation
    norl = df.copy()
    norl[1:]=(df[1:].values/df[0:1].values)
    norl.ix[0,:]=0
    #norl = norl*allocation
    return daily_ret,cum_ret,norl
    
def SR_f(X,daily_ret):
    port_ret = (X*daily_ret).sum(axis=1)
    Y = -port_ret.mean()/port_ret.std()*math.sqrt(252)
    #print 'X={}, Y={}'.format(X,Y)
    #print type(Y)
    return Y
    
def Clean_Data(name):
    df = pd.read_csv(name)
    #print df.index
    buf = df.columns[0]
    y = re.findall('[A-Z.]+',buf)

    dates = []
    for i in range(0,len(df)):
        date_buf = pd.Timestamp(df.ix[i][0][0:11])
        dates.append(date_buf)    
    ts = pd.Series(np.random.randn(len(df)), dates)  
    #start_date = df.ix[0][0][0:11]
    #end_date = df.ix[len(df)-1][0][0:11]
    #dates = pd.date_range(start_date,end_date)
    #print type(dates)

    #print df.columns[0]
    cols =re.findall('[A-Z]+',df.columns[0])
    #print y
    B = np.array([0,0,0,0])
    for item in df.index:
        buf = df.ix[item][0][11:]
        y = re.findall('[0-9.]+',buf)
        c = [float(i) for i in y]
        A = np.array(c)
        B = np.vstack((B,A)) 
    bbb=  B[1:][:]
    #print len(dates)

    df1=pd.DataFrame(bbb,index=dates,columns=cols[1:])
    return df1
#print df1.head()
#df1.plot()
#aa = np.array([[1,2,3,4],[2,3,4,5]])
allocate=np.array([0.1,0.0,0.9,0.0])
name = 'result.csv'
df1 = Clean_Data(name)

total_amount=1000000
daily_ret,cum_ret,pos_vals = assess_portfolio(df1)
#daily_spy,cum_spy,pos_vals_spy = assess_portfolio(df_spy)
#print df2.mean()
print 'Standard deviation of daily return:'
print daily_ret.std()
pos_vals = pos_vals*total_amount*allocate
 
aaa = pos_vals[len(df1)-1:len(df1)]
print 'Remaining amount: $', aaa.sum(axis=1).values
port_daily_ret = (daily_ret*allocate).sum(axis=1)
#normalized = pd.DataFrame([0])
normalized = pos_vals.sum(axis=1)/total_amount
#print normalized.index
normalized.plot(label='Portfolio')
#normalized.columns=['portfolio']
sharp_ratio = port_daily_ret.mean()/port_daily_ret.std()*math.sqrt(252)
print 'Portfolio sharp ratio =',sharp_ratio
sharp_ratio = daily_ret['GOOG'].mean()/daily_ret['GOOG'].std()*math.sqrt(252)
print 'GooG sharp ratio = ',sharp_ratio
sharp_ratio = daily_ret['AAPL'].mean()/daily_ret['AAPL'].std()*math.sqrt(252)
print 'AAPL sharp ratio = ',sharp_ratio
sharp_ratio = daily_ret['XOM'].mean()/daily_ret['XOM'].std()*math.sqrt(252)
print 'XOM sharp ratio = ',sharp_ratio
sharp_ratio = daily_ret['GLD'].mean()/daily_ret['GLD'].std()*math.sqrt(252)
print 'GLD sharp ratio = ',sharp_ratio
print type(sharp_ratio)

(cum_ret['GOOG']+1).plot()
(cum_ret['GLD']+1).plot()
(cum_ret['AAPL']+1).plot()
(cum_ret['XOM']+1).plot()
#(cum_spy+1).plot()
plt.ylim(ymax = 1.4, ymin = 0.8)
plt.legend(loc='upper left')
plt.ylabel('Normalized price')
plt.xlabel('Timeline')

Xguess = np.array([.25,.25,.25,.25])
#YY = SR_f(Xguess,daily_ret)
#print YY
bnds = ((0, 1.), (0, 1.),(0,1.),(0,1.),(0,1.))
cons = ({'type': 'eq', 'fun': lambda x:  1 - sum(x)})
bnds = tuple((0,1) for x in Xguess)
min_result = spo.minimize(SR_f, Xguess, args=daily_ret, method='SLSQP', options={'disp':True},bounds=bnds ,constraints=cons)
#res = minimize(getSharpe, start_pos, method='SLSQP', bounds=bnds ,constraints=cons)
print 'Minima found at:'
print 'X={},Y={}'.format(min_result.x,min_result.fun)


#df3.plot()