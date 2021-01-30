# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:47:11 2020

@author: syahr
"""

import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return x**2 - 16


xi = -8.0
xf = 3.0
tol = 1.0e-5
niter = 1000

if func(xi)*func(xf) > 0:
    print('tidak punya akar pada rentang tersebut')
else:
    for i in range(niter):
        xb = 0.5*(xi+xf)
        if func(xi)*func(xb) < 0:
            xf = xb
        else:
            xi = xb
        
        if abs(xi-xf) < tol:
            akar = xb
            print('perhitungan convergence ','pada iter-ke ',i)
            print(akar)
            break
        
            
