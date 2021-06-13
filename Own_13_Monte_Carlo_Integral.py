# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 23:12:43 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**(np.sin(x)) + 2.0

a = 1.0
b = 25.0
n = 1000

xx = np.linspace(a,b,n)
yy = func(xx)
ymax = np.max(yy)

dalam = 0.0
xin = []
yin = []
xout = []
yout = []
for i in range(n):
    x = np.random.uniform(a,b)
    y = np.random.uniform()*ymax
    if y <= func(x):
        dalam = dalam + 1
        xin.append(x)
        yin.append(y)
    else:
        xout.append(x)
        yout.append(y)
        
luas_pp = (b-a)*ymax
hasil = (dalam/n)*luas_pp

print(hasil)

plt.plot(xin,yin,'x',color='red')
plt.plot(xout,yout,'x',color='blue')
plt.plot(xx,func(xx),color='black')
plt.show()


