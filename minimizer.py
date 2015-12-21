# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:43:41 2015

@author: xiaoqin
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
    Y = (X[0]-1.5)**2 +0.5+(X[1]-3)**2
    print 'X={}, Y={}'.format(X,Y)
    return Y
    
def test_run():
    Xguess = np.array([2.,2.])
    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp':True})
    print 'Minima found at:'
    print 'X={},Y={}'.format(min_result.x,min_result.fun)
    
    #plot
    Xplot = np.linspace(0.5,2.5,21)
    Yplot = f(Xplot)
    plt.plot(Xplot,Yplot)
    plt.plot(min_result.x,min_result.fun,'ro')
    plt.title("Minima of the function")
    plt.show()


if __name__=="__main__":
    test_run()