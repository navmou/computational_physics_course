
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

d = np.loadtxt('task4/positions.txt')

M = d.shape[0]-10000

plt.figure(figsize=(23,19))


c_n = []
for l in range(1000):
    c_l = []
    for p in range(5):
        pos = d[10000:,p]
        c = 0
        for m in range(M-l-1):
            c += (pos[m+l] - pos[m])*(pos[m+l] - pos[m])
    
        c_l.append(c/(M-l))   
    
    c_n.append(np.average(c_l))



plt.loglog(c_n)
    
plt.grid()

D = []
for i in range(len(c_n)):
    D.append(c_n[i]/(6*i))
plt.figure()
plt.plot(D)
plt.grid()
