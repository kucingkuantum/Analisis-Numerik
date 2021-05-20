# -*- coding: utf-8 -*-
"""
Created on Wed May 19 12:56:31 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

def func(y,v,t):
    return v - 3*y + t

t0 = 0.0
tn = 4.0
y0 = 1.0
v0 = -2.0
ndata = 100
t = np.linspace(t0,tn,ndata)

y = np.zeros(ndata)
y[0] = y0
v = np.zeros(ndata)
v[0] = v0
h = t[2] - t[1]

for i in range(0,ndata-1):
    y[i+1] = y[i] + h*v[i]
    v[i+1] = v[i] + h*func(y[i],v[i],t[i])
    
plt.figure(1)
plt.title('Y Euler utk ODE-2')
plt.plot(t,y)
plt.legend()

plt.figure(2)
plt.title('V Euler utk ODE-2')
plt.plot(t,v)
plt.show()




