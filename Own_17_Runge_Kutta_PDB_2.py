# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:07:04 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

def func(y,z,t):
    return z

def gunc(y,z,t):
    return z - 3*y + t

y0 = 1.0
t0 = 0.0
tn = 10.0
ndata = 1000
t = np.linspace(t0,tn,ndata)

h = t[2] - t[1]

z0 = -2.0

y = np.zeros(ndata)
y[0] = y0 

z = np.zeros(ndata)
z[0] = z0


for i in range(ndata-1):
    k1 = h*func(y[i],z[i],t[i])
    l1 = h*gunc(y[i],z[i],t[i])
    
    k2 = h*func(y[i]+0.5*h,z[i]+0.5*l1,t[i]+0.5*k1)
    l2 = h*gunc(y[i]+0.5*h,z[i]+0.5*l1,t[i]+0.5*k1)
    
    k3 = h*func(y[i]+0.5*h,z[i]+0.5*l2,t[i]+0.5*k2)
    l3 = h*gunc(y[i]+0.5*h,z[i]+0.5*l2,t[i]+0.5*k2)
    
    k4 = h*func(y[i]+h,z[i]+l3,t[i]+k3)
    l4 = h*gunc(y[i]+h,z[i]+l3,t[i]+k3)

    l = (l1 + 2.0*l2 + 2.0*l3 + l4)/6.0
    k = (k1 + 2.0*k2 + 2.0*k3 + k4)/6.0
    
    y[i+1] = y[i] + k
    z[i+1] = z[i] + l


plt.plot(t,y)
plt.plot(t,z)

plt.show()
















