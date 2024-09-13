#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:12:33 2020

@author: navid
"""


import numpy as np
import matplotlib.pyplot as plt

#loading data
c_l_solid = np.loadtxt('c_l_solid.txt')
c_l_liquid = np.loadtxt('c_l_liquid.txt')


plt.figure(figsize=(15,10))
plt.grid()
dt = 0.001


#calculating the self Diffusion coefficient
D1 = []
D2 = []
for i in range(len(c_l_solid)):
    D1.append(c_l_solid[i]/(6*i*dt))
    D2.append(c_l_liquid[i]/(6*i*dt))

#Plotting self Diffusion coefficient
plt.figure()
plt.plot(D1)
plt.plot(D2)
plt.grid()
plt.xlabel('Lag time' , fontsize=18)
plt.ylabel('Self diffusion coefficient', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xticks(np.arange(0,5001, 200) , np.arange(0,5001,200)*dt)



#Plotting MSD
plt.figure(figsize=(15,10))
plt.plot(c_l_solid[0:1000], label = 'Solid' , color = 'blue')
plt.plot(c_l_liquid[0:1000], label = 'Liquid' , color = 'red')
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.ylabel(r'MSD ($\AA^2$)', fontsize = 18)
plt.xlabel('Lag time (ps)', fontsize=18)
plt.xticks(np.arange(0,1001, 200) , np.arange(0,1001, 200)*dt)
plt.legend(prop={"size":20})
plt.grid()


z = np.polyfit(np.arange(100,1000)*dt,c_l_liquid[100:1000],1)



phi_solid = np.loadtxt('v_l_solid.txt')
phi_liquid = np.loadtxt('v_l_liquid.txt')
#Plotting velocity correlation 
plt.figure(figsize=(15,10))
plt.plot(phi_solid[0:1000]/phi_solid[0] , label = 'Solid' , color = 'blue')
plt.plot(phi_liquid[0:1000]/phi_liquid[0] , label = 'Liquid' , color = 'red')
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.ylabel(r'$\phi(t)/\phi(0)$', fontsize = 18)
plt.xlabel('Lag time (ps)', fontsize=18)
plt.xticks(np.arange(0,1001, 200) , np.arange(0,1001, 200)*dt)
plt.legend(prop={"size":20})
plt.grid()




#Calculating the spectral function
phi_omega_liq = []

omega_ = np.linspace(0,0.2, 150)
for omega in omega_:
    s = 0
    for t in range(450):
        s += 2*phi_liquid[t]*np.cos(omega*t)*dt
        
    phi_omega_liq.append(s)
    
#plotting spectral function for liquid phase
plt.figure(figsize=(15,10))
plt.plot(phi_omega_liq, color = 'red', linewidth = 1, label='Liquid')
#plt.xticks(np.arange(0,5001,2500), [r'$0$' , r'$\pi/2$' , r'$\pi$'])
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlabel(r'$\omega$', fontsize=18)
plt.ylabel(r'$\hat{\phi}(\omega)$', fontsize=18)


print(f'Self diffusion coefficient is: {phi_omega_liq[0]/6}')


#Calculating the spectral function for solid
phi_omega = []

omega_ = np.linspace(0,0.2, 150)
for omega in omega_:
    s = 0
    for t in range(450):
        s += 2*phi_solid[t]*np.cos(omega*t)*dt
        
    phi_omega.append(s)

#plotting the spectral function for solid
plt.figure(figsize=(10,15))
plt.plot(phi_omega, color = 'blue' , linewidth=1, label='Solid')
#plt.xticks(np.arange(0,5001,2500), [r'$0$' , r'$\pi/2$' , r'$\pi$'])
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlabel(r'$\omega (\tau^{-1})$', fontsize=18)
plt.ylabel(r'$\hat{\phi}(\omega)(\AA^{2}\tau)$', fontsize=18)

plt.xlim(0,150)
plt.legend(prop={"size":20})
plt.ylim(0,7.5)




#Calculation of the power spectrum
P_omega = np.array(phi_omega)*np.array(phi_omega)
plt.plot(P_omega)



hey = np.fft.ifft(P_omega)
plt.figure()
plt.plot(hey)














