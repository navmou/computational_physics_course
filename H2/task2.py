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



k_b = 8.61733034*10**-5


#Loading Data
d = np.loadtxt('average_values.txt')


T = d[:,0]
E= d[:,1]
E_sq = d[:,2]
n = d[:,3]
n_sq = d[:,4]
Nab = d[:,7]
Nab_sq = d[:,8]




#Calculation of sigma and heat capacity
C = []
sigma_E = []
sigma_n = []
sigma_Nab = []
for i in range(len(T)):
    C.append((E_sq[i] - (E[i]*E[i]))/(k_b*T[i]*T[i]))
    sigma_E.append(np.sqrt(E_sq[i] - (E[i]*E[i])))
    sigma_n.append(np.sqrt(n_sq[i] - (n[i]*n[i])))
    sigma_Nab.append(np.sqrt(Nab_sq[i] - (Nab[i]*Nab[i])))
    






error_E = sigma_E/np.sqrt(1000000/1232)
error_n = sigma_n
error_Nab = sigma_Nab

plt.figure(figsize=(15,10))
#plt.errorbar(T , E, yerr=error_E, uplims=True, lolims=True , label='MC Simulation')
plt.plot(T , E, label='MC Simulation')
plt.ylabel('Energy (eV)')
plt.xlabel('Temperature (K)')
plt.plot(np.ones(50)*741.15 ,  np.linspace(-2350,-2280) , 'r--' , label = r'Experimental $T_c = 741.15$ K')
plt.grid()
plt.legend()
plt.savefig('E_T.png', dpi = 100)




#Plotting Heat Capacity
plt.figure(figsize=(17,13))
plt.plot(T , C , '.--' , label='MC Simulation')
plt.xlabel('Temperature (K)')
plt.ylabel('C(T) (eV/K)')
plt.plot(np.ones(50)*741.15 ,  np.linspace(-0.5,0.5) , 'r--' , label = r'Experimental $T_c = 741.15$ K')
plt.grid()
plt.legend()
plt.ylim(-0.01,0.45)
plt.savefig('C_T.png', dpi = 100)




#Plotting long range correlation P(T) 
N = 1000
P = []
for i in range(len(T)):
    P.append((2*n[i]/N)-1)

plt.figure(figsize=(17,13))
#plt.errorbar(T,P, yerr=error_n, uplims=True, lolims=True , label='MC Simulation')
plt.plot(T,P, '.--',label='MC Simulation')
plt.xlabel('Temperature (K)')
plt.ylabel('P(T)')
plt.plot(np.ones(50)*741.15 ,  np.linspace(-0.7,1.5) , 'r--' , label = r'Experimental $T_c = 741.15$ K')
plt.grid()
plt.legend()
plt.ylim(-0.5,1.1)
plt.savefig('P_T.png', dpi = 100)




#Plotting short range correlation r(T)
N = 1000
r = []
for i in range(len(T)):
    r.append((Nab[i]-4*N)/(4*N))

plt.figure(figsize=(17,13))
#plt.errorbar(T,r, yerr=error_Nab, uplims=True, lolims=True , label='MC Simulation')
plt.plot(T,r, '.--', label='MC Simulation')
plt.plot(np.ones(50)*741.15 ,  np.linspace(0.0,1.1) , 'r--' , label = r'Experimental $T_c = 741.15$ K')
plt.xlabel('Temperature (K)')
plt.ylabel('r(T)')
plt.grid()
plt.legend()
plt.ylim(0,1.1)
plt.savefig('r_T.png', dpi = 100)











for temp in T:
    b = np.loadtxt(f'Temp_{int(temp)}_EQ.txt')
    with open(f'new_data/energy_{temp}.txt' , 'w') as fuc:
        for i in b[:,3]:
            fuc.write(f'{i}\n')
    with open(f'new_data/Nab_{int(temp)}.txt' , 'w') as fuc:
        for i in b[:,2]:
            fuc.write(f'{i}\n')
    with open(f'new_data/n_{int(temp)}.txt' , 'w') as fuc:
        for i in b[:,4]:
            fuc.write(f'{i}\n')







c = np.loadtxt("corr.txt")
plt.figure(figsize=(17,12))
plt.plot(c[:,0] , c[:,1])
plt.xlabel('k')
plt.ylabel(r'$\phi_{k}$' )
plt.plot(np.ones(1213)*0.135 , '--', color='orange')
plt.plot(np.ones(50)*1213, np.linspace(0,0.135,50) , '--', color='orange')

plt.ylim(0,1)
plt.xticks(np.arange(0,1501,500))
plt.xticks(list(plt.xticks()[0]) + [1213])
plt.yticks(list(plt.yticks()[0]) + [0.135])
plt.xlim(0, 1500)
plt.savefig('Correlation.png', dpi=100)



c = np.loadtxt("block.txt")
plt.figure(figsize=(15,10))
plt.plot( c[:,2] , c[:,3] , 'o')

plt.xlabel(r'$\sqrt{Block size}$' )
plt.ylabel(r'$n_{s}$')
plt.plot(np.ones(150)*1213, '--' , label='Correlation result')
plt.tick_params(axis='both', which='major')
plt.tick_params(axis='both', which='minor')
plt.yticks([0,500,1012,1213] )
plt.xlim(0,700)
z = np.polyfit(c[700:5000,2],c[700:5000,3],1)

p = np.poly1d(z)
x = np.linspace(0,700)
plt.plot(x , p(x) , '--' , label='Polynomial fit')
plt.legend(prop={'size':20})

plt.savefig('box_avg.png',dpi=100)






plt.figure(figsize=(15,10))
for t in [0,200,500,750,1000]:
    d = np.loadtxt(f"Temp_{t}.txt")
    plt.plot(d[:,3], label=f'T = {t} K')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Energy (eV)')





