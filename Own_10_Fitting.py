# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:54:15 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def func(x,a,b,c,d):
    return a*np.sin(b*x + c ) + d

filename = 'input.xls'
raw = pd.read_excel(filename)

xraw = raw.iloc[:,0]
yraw = raw.iloc[:,1]

tebakan = [2,1.0,10,80]
best_val,covar = curve_fit(func,xraw,yraw,p0=tebakan)
print(best_val)



r2 = r2_score(yraw, func(xraw,*best_val))

plt.plot(xraw,yraw,'x',label='Experiment')
plt.plot(xraw,func(xraw,*best_val),label='fit' + 
         'R2 = '+str(r2))   
plt.legend()
plt.show()

