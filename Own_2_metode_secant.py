# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:58:28 2020

@author: syahr
"""

import numpy as np

def func(x):
    return 2*x**3 + (5*x**2)*np.exp(0.1*x) + 100

xm1 = -1
xn = 5
tol = 1.0e-7
maxiter = 5000

for iter in range(maxiter):
    xp1 = xn - ((xn-xm1)*func(xn)/(func(xn)-func(xm1)))
    if abs(func(xp1)) < tol:
        akar = xp1
        print('solusi =',akar)
        print('converged pada iterasi =',iter)
        break
    else:
        xm1 = xn
        xn = xp1
        
        


