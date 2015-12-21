# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:22:55 2015

@author: xiaoqin
"""

import numpy as np

def test_np():
    np.random.seed(149)
    #a = np.ones((5,3),dtype=np.int_)
    #a = np.random.normal(0,5,size = (4,3))    
    #a = np.random.randint(0,10,size=(4,5))     
    a = np.array([(1,2,3),(3,4,5)])    
    print a*2
    #print a.sum()
    #print a.sum(axis=0)
    #print a.sum(axis=1)
    #print np.nanargmax(a)

if __name__ == "__main__":
    test_np()