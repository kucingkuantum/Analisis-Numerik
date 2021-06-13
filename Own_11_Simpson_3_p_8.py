# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:43:24 2021

@author: user
"""
import numpy as np

def func(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10.0    
N = 3000

h = (b-a)/N
x = np.linspace(a,b,N+1)

dalam = func(a) + func(b)
for i in range(1,N):
    if np.mod(i,3) == 0:
        dalam = dalam + 2.0*func(x[i])
    else:
        dalam = dalam + 3.0*func(x[i])
    
hasil = (3.0*h/8.0)*dalam
print(hasil)





