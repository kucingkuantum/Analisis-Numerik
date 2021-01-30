# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:17:58 2020

@author: syahr
"""
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10
n = 15

x = np.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0
for iter in range(n-1):
    hasil += dx*func(x[iter])

print('hasil integral =', hasil)

xp = np.linspace(a,b,1000)

plt.plot(xp,func(xp),color='blue')
for i in range(n):
    plt.bar(x[i],func(x[i]),align='edge',width=dx,color='gray',edgecolor='r')
    
plt.show()
















