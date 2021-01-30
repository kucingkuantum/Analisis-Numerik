# -*- coding: utf-8 -*-
"""
Created on Sat May 30 01:07:42 2020

@author: syahr
"""
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10.0
n = 500

dx = (b-a)/(n-1)
x = np.linspace(a,b,n)

sum = 0.0
for i in range(1,n-1):
    sum += func(x[i])

hasil = 0.5*dx*(func(x[0])+
                2.0*sum+func(x[-1]))

print(hasil)
nd = 1000
xp = np.linspace(a,b,nd)

plt.plot(xp,func(xp))
for i in range(n):
    plt.bar(x[i],func(x[i]),
            align='edge',
            width=0.000001,
            color='gray',
            edgecolor='red')

plt.fill_between(x,func(x),
                 color='gray')


plt.show()
















