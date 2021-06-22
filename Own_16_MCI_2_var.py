# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:58:01 2021

@author: user
"""
import numpy as np

def func(x,y):
    return 1.0 - x**2 - y**2

a = 0.0
b = 1.0
c = 0.0
d = 5.0
N = 100000
x = np.random.uniform(a,b,N)
y = np.random.uniform(c,d,N)

frata = np.mean(func(x,y))
hasil = (b-a)*(d-c)*frata

print(hasil)

