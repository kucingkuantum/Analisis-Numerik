# -*- coding: utf-8 -*-
"""
Created on Tue May 19 16:43:16 2020

@author: syahr
"""

def func(x):
    return x**2 - x - 12.0

def tur(x):
    return 2*x - 1.0

xn = 30.0
tol = 1.0e-10
maxiter = 200
for iter in range(maxiter):
    xp = xn - func(xn)/tur(xn)
    if abs(func(xp)) < tol:
        solusi = xp
        print('solusi =',solusi)
        print('convergence pada',iter)
        break
    else:
        xn = xp
        








