import numpy as np
import matplotlib.pyplot as plt

def func(N,t):
    k = 0.02
    return -k*N

# Initial COndition / Boundary COndition
N0 = 1000
t0 = 0

#Proses diskritisasi
ndata = 70
tn = 100
t = np.linspace(t0,tn,ndata)
N = np.zeros(ndata)
N[0] = N0
h = t[1] - t[0]
# proses Euler
for i in range(0,ndata-1):
    N[i+1] = N[i] + h*func(N[i],t[i])

# Fungsi Analitik
k = 0.02
NA = N0*np.exp(-k*t)

#Plot
plt.plot(t,NA,'red',label='analitik')
plt.plot(t,N,'x',color= 'black',label='Euler')    
plt.legend()
plt.show()    












