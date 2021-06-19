# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:53:36 2021

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

filename ='data_luas.xlsx'
raw = pd.read_excel(filename)
x = raw.iloc[:,0]
y = raw.iloc[:,1]


# Luas dengan Internal Numpy
luas_np = np.trapz(y,x)
print('luas np =',luas_np)

# Luas dengan Implementasi Trapezoid
dx = x[2]-x[1]
ndata = len(x)

sum = 0.0
for i in range(1,ndata-1):
    sum += y[i]

luas_im = 0.5*dx*(y[0]+2.0*sum+
                  y[ndata])

print('luas im =',luas_im)



# plt.plot(x,y)
# plt.show()





