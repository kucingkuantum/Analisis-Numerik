# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:15:14 2021

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt

def anali(x):
    return 14.5 * np.exp(-x) + 0.5*x - 4.5


def func(x,y):
    return 0.5*x - y - 4.0
# Numerical parameter
ndata = 1000

# Physical Parameter
x0 =0.0
xn = 20.0
y0 =10.0

x = np.linspace(x0,xn,ndata)
y = np.zeros(ndata)
y[0] = y0

h = x[2] - x[1]

for i in range(ndata-1):
    k1 = func(x[i],y[i])
    k2 = func(x[i]+0.5*h,y[i]+h+0.5*k1)
    k3 = func(x[i]+0.5*h,y[i]+h+0.5*k2)
    k4 = func(x[i]+h,y[i]+h*k3)
    
    y[i+1] = y[i] + h*(k1+2*k2+2*k3+k4)/6.0
    

plt.plot(x,y,label='Runge-Kutta 4')
plt.plot(x,anali(x),label='analitis')
plt.legend()
plt.show()







