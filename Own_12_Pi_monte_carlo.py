# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 23:26:18 2021

@author: user
"""

import numpy as np 
import matplotlib.pyplot as plt
from decimal import Decimal


def line_circle(x):
    return np.sqrt(1-x**2)


ndata = 2000


dalam = 0
xin = []
yin = []
xout = []
yout = []
for i in range(ndata):
    x = np.random.uniform()
    y = np.random.uniform()
    if x**2 + y**2 <= 1:
        dalam = dalam + 1
        xin.append(x)
        yin.append(y)
    else:
        xout.append(x)
        yout.append(y)


pi = 4.0*dalam/ndata 

print('pi =',Decimal.from_float(pi))

plt.plot(xin,yin,'x')
plt.plot(xout,yout,'o')
plt.plot(np.linspace(0,1,100),line_circle(np.linspace(0,1,100)),'k')
plt.show()

        
        

    