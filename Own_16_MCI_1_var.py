# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 13:41:57 2021

@author: user
"""
import numpy as np

def func(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10.0
N = 100000
x = np.random.uniform(a,b, N)

frata = np.mean(func(x))
hasil = (b-a)*frata
print(hasil)





