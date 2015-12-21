# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 23:32:54 2015

@author: xiaoqin
"""

from numpy import arange, sin, pi, random, array
x = arange(0, 6e-2, 6e-2 / 30)
A, k, theta = 10, 1.0 / 3e-2, pi / 6
y_true = A * sin(2 * pi * k * x + theta)
y_meas = y_true + 2*random.randn(len(x))
print 'y_meas:',y_meas

def residuals(p, y, x):
    A, k, theta = p
    err = y - A * sin(2 * pi * k * x + theta)
    return err
    
def peval(x, p):
    return p[0] * sin(2 * pi * p[1] * x + p[2])

p0 = [8, 1 / 2.3e-2, pi / 3]
print(array(p0))

from scipy.optimize import leastsq
plsq = leastsq(residuals, p0, args=(y_meas, x))
print(plsq[0])

print(array([A, k, theta]))