#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 13:22:40 2020

@author: navid
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



mpl.rcParams['figure.titlesize'] = 25 
mpl.rcParams['lines.linewidth'] = 1.5
mpl.rcParams['axes.labelsize'] = 22 
mpl.rcParams['xtick.labelsize'] = 22 
mpl.rcParams['ytick.labelsize'] = 22 
mpl.rcParams['legend.fontsize'] = 22


E = np.loadtxt("E.txt")
N = np.loadtxt("N.txt")
dt = 0.01

#Plotting energy
plt.figure(figsize=(10,7))
plt.plot(E , label = 'Simulation')
plt.plot(np.linspace(0,len(E), 50) , -2.9*np.ones((50)) , 'r--' , label = r'Experiment (E = $-2.9$)')
#plt.xlim(-1000,len(E))
#plt.ylim(0,1)
plt.legend()
plt.xlabel('Iteration')
plt.ylabel(r'$E_\tau$ (Hartree)')
plt.savefig('energy-total.png', dpi = 100)



plt.figure(figsize=(10,7))
plt.plot(E[:5000], label = 'Simulation')
plt.plot(np.linspace(0,5000, 50) , -2.9*np.ones((50)) , 'r--' , label = r'Experiment (E = $-2.9$)')
#plt.xlim(-1000,len(E))
#plt.ylim(0,1)
plt.legend()
plt.xlabel('Iteration')
plt.ylabel(r'$E_\tau$ (Hartree)')
plt.xticks(np.arange(0,5001 , 1000))
plt.savefig('energy-equilibration.png', dpi = 100)



plt.figure(figsize=(10,7))
plt.plot(E[5000:], label = rf'$\langle E \rangle$ = {np.average(E[15000:])}')
plt.plot(np.linspace(0,len(E)-5000, 50) , -2.9*np.ones((50)) , 'r--' , label = r'Experiment (E = $-2.9$)')
#plt.xlim(-1000,len(E))
#plt.ylim(0,1)
plt.legend()
plt.xlabel('Iteration')
plt.ylabel(r'$E_\tau$ (Hartree)')
plt.xticks(np.arange(0,45001 , 10000),np.arange(5000,50001, 10000))
plt.ylim(-4, -1.5)
plt.savefig('energy-eqilibrium.png', dpi = 100)





#Plotting N
plt.figure(figsize=(10,7))
plt.plot(N, label = 'Simulation')
plt.xlabel('Iteration')
plt.ylabel('Number of walkers')
plt.plot(np.linspace(0,len(E), 50) , 500*np.ones((50)) , 'r--' , label = r'$N_0 = 500$')
plt.legend()
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.ylim(450,650)
plt.savefig('N.png', dpi = 100)


plt.figure(figsize=(10,7))
plt.plot(N[:5000], label = 'Simulation')
plt.xlabel('Iteration')
plt.ylabel('Number of walkers')
plt.plot(np.linspace(0,5000, 50) , 500*np.ones((50)) , 'r--' , label = r'$N_0 = 500$')
plt.legend()
plt.xticks(np.arange(0,5001 , 1000))
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.ylim(450,650)
plt.savefig('N-equilibration.png', dpi = 100)


plt.figure(figsize=(10,7))
plt.plot(N[5000:] , label = rf'$\langle N \rangle$ = {np.average(N[15000:])}')
plt.xlabel('Iteration')
plt.ylabel('Number of walkers')
plt.plot(np.linspace(0,len(E)-5000, 50) , 500*np.ones((50)) , 'r--' , label = r'$N_0 = 500$')
plt.legend()
plt.xticks(np.arange(0,45001 , 10000),np.arange(5000,500010, 10000))
plt.ylim(350,650)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.savefig('N-equilibrium.png', dpi = 100)



print(np.average(E[15000:]))
print(np.average(N[15000:]))
