# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:24:04 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

# initial condition 
t0 = 0
tn = 300
ndata = 1000

t = np.linspace(t0,tn,ndata)
h = t[2] - t[1]
N = 1000
I0 = 1
R0 = 0
S0 = N - I0 - R0

I=np.zeros(ndata)
S=np.zeros(ndata)
R=np.zeros(ndata)

I[0]=I0
R[0]=R0
S[0]=S0

beta = 0.2
gamma = 0.1


for ii in range(0,ndata-1):
    S[ii+1]=S[ii] - h*beta*S[ii]*I[ii]/N
    I[ii+1]=I[ii] + h*beta*S[ii]*I[ii]/N - h*gamma*I[ii]
    R[ii+1]=R[ii] + h*gamma*I[ii]

plt.plot(t,S,label='S')
plt.plot(t,I,label='I')
plt.plot(t,R,label='R')
plt.legend()
plt.show()    












