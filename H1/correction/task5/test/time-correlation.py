
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:48:44 2020

@author: navid
"""
import numpy as np
import matplotlib.pyplot as plt

#Task 5
#loading data
c_n = np.loadtxt('c_l.txt')
c_n_liq = np.loadtxt('c_l_liq.txt')


plt.figure(figsize=(15,10))
plt.grid()
dt = 0.001
D1 = []
D2 = []
for i in range(len(c_n)):
    D1.append(c_n[i]/(6*i*dt))
    D2.append(c_n_liq[i]/(6*i*dt))




plt.figure()
plt.plot(D1)
plt.plot(D2)
plt.grid()
plt.xlabel('Lag time' , fontsize=18)
plt.ylabel('Self diffusion coefficient', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(np.arange(0,5001, 1000) , np.arange(0,5001,1000)*dt)






plt.figure(figsize=(15,10))
plt.plot(c_n/10000 , label = 'Solid' , color = 'blue')
plt.plot(c_n_liq/10000, label = 'Liquid' , color = 'red')
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.ylabel(r'MSD ($\AA$)', fontsize = 18)
plt.xlabel('Lag time (ps)', fontsize=18)
plt.xticks(np.arange(0,5001, 1000) , np.arange(0,5001, 1000)*dt)
plt.legend(prop={"size":20})
plt.grid()





with open("c_n.txt" , "w") as f:
    for i in range(len(c_n)):
        f.write(f'{c_n[i]}\n')