
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:48:44 2020

@author: navid
"""
import numpy as np
import matplotlib.pyplot as plt

#Task 5


# Calculation of position time correlation

d = np.loadtxt('solid/r.txt')

M = d.shape[0]-10000




c_n = []
for l in range(1000):
    c_l = []
    for p in range(256):
        pos = d[10000:,p]
        c = 0
        for m in range(M-l-1):
            c += (pos[m+l] - pos[m])*(pos[m+l] - pos[m])
    
        c_l.append(c/(M-l))   
    
    c_n.append(np.average(c_l))




c_n = np.loadtxt('c_n.txt')
    
plt.figure(figsize=(15,10))
plt.grid()
dt = 0.001
D = []
for i in range(len(c_n)):
    D.append(c_n[i]/(6*i*5*dt))
plt.figure()
plt.plot(D)
plt.grid()
plt.xlabel('Lag time' , fontsize=18)
plt.ylabel('Self diffusion coefficient', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(np.arange(0,1001, 200) , np.arange(0,1001,200)*dt)


plt.figure(figsize=(15,10))
plt.plot(c_n , label = 'Liquid')
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.ylabel(r'MSD ($\AA$)', fontsize = 18)
plt.xlabel('Lag time (ps)', fontsize=18)
plt.xticks(np.arange(0,1001, 200) , np.arange(0,1001,200)*dt)
plt.legend(prop={"size":20})
plt.grid()





with open("c_n.txt" , "w") as f:
    for i in range(len(c_n)):
        f.write(f'{c_n[i]}\n')