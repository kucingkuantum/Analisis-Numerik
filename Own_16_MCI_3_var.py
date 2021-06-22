# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:09:40 2021

@author: user
"""

import numpy as np

def func(x,y,z):
    return x*y/z

N = 10000
a = 4.0
b = 7.0
x = np.random.uniform(a,b,N)

c = 3.0
d = 5.0
y = np.random.uniform(c,d,N)

e = 1.0
f = 2.0
z = np.random.uniform(e,f,N)

frata = np.mean(func(x,y,z))
hasil = frata*(b-a)*(d-c)*(f-e)

print(hasil)