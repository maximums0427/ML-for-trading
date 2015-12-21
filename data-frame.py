# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:23:53 2015

@author: xiaoqin
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def symbol_to_path(symbol):
    """Return CSV file path given ticker symbol."""
    return os.path.join("{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    if 'spy' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'spy')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        path = symbol_to_path(symbol)
        df_temp = pd.read_csv(path,index_col = "Date", parse_dates = True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close':symbol})
                
        df = df.join(df_temp,how='inner')
       
    return df
    
def daily_return(df):
    daily_ret = df.copy()
    daily_ret.ix[1:,:] = df.ix[1:,:]/df.ix[:-1,:].values-1
    daily_ret.ix[0,:]=0
    return daily_ret


def test_run():
    # Define a date range
    dates = pd.date_range('2008-01-01', '2010-01-31')

    # Choose stock symbols to read
    symbols = ['spy', 'ibm', 'luv', 'grr']
    
    # Get stock data
    df = get_data(symbols, dates)
    daily_ret = daily_return(df)
    print daily_ret.head()
    #df = df[::-1]
    #df = df/df.ix[0]
    #print df.ix['2009-01-12'] 
    #print df.ix[0,:]
    #print 'Mean:\n', df.mean()
    #print 'Median:\n', df.median()
    #print 'std:\n', df.std()
    #ax = daily_ret.plot()
    #rm = pd.rolling_mean(df['spy'],window=20)
    #rstd = pd.rolling_std(df['spy'],window=20)
    #upper_band = rm+2*rstd
    #lower_band = rm-2*rstd
    
    #upper_band.plot(ax=ax)
    #lower_band.plot(ax=ax)
    
    daily_ret['spy'].hist(bins=20,label='SPY')
    daily_ret['ibm'].hist(bins=20,label='IBM')
    plt.legend(loc='upper right')
    plt.show()     
    print 'SPY:',daily_ret['spy'].mean()
    print 'IBM:',daily_ret['ibm'].mean()
    #print df
    #print df.ix['2008-01-01']
    #print df.head()
    daily_ret.plot(kind='scatter',x='spy',y='ibm')
    plt.grid()
    plt.axis('equal')
    beta,alpha = np.polyfit(daily_ret['spy'],daily_ret['ibm'],1)
    #buf = np.array([range(10,2)]   
    plt.plot(daily_ret['spy'],beta*daily_ret['spy']+alpha,'-',color='r')
    print 'beat:',beta 
    daily_ret.plot(kind='scatter',x='spy',y='luv')
    print daily_ret.corr(method = 'pearson')
    


if __name__ == "__main__":
    test_run()
