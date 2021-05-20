# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:24:15 2021

@author: Syahril Siregar
"""
import numpy as np

def func(x):
    return (x**2)*np.exp(-x)

a = 1.0
b = 10.0
N = 5000

h = (b-a)/N
x = np.linspace(a,b,N+1)

sum_genap = 0.0
sum_ganjil = 0.0
for i in range(1,N):
    if np.mod(i,2) == 0:
        sum_genap = sum_genap + 2*func(x[i])
    else:
        sum_ganjil = sum_ganjil + 4*func(x[i]) 

hasil = (h/3)*(func(a)+sum_ganjil+sum_genap
               +func(b))

print(hasil)


















