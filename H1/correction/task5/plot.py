#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:08:59 2020

@author: navid
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

#Plotting task 1 energy vs vol
d = np.loadtxt("energy.txt")

x = d[:,0]**3
y = d[:,1]/64
z = np.polyfit(x,y,2)
p = np.poly1d(z)

fig, ax = plt.subplots()

ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
plt.scatter(x, y)
plt.xlabel(r'Volume ($\AA^3$)', fontsize=18)
plt.ylabel('Energy (eV/unit cell)',fontsize=18)
plt.plot(np.linspace(64,69),p(np.linspace(64,69)), 'r--' )
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.grid()
plt.savefig('task1.png')



#Loading data
d = np.loadtxt("solid/energies.txt")

#Plotting Energies
##Kinetic 
plt.figure(figsize=(10,9))
t = len(d[:,0])
n_points = t/10
dt = 0.001
plt.plot(d[:,0], label = 'Kinetic Energy')
plt.legend(prop={"size":20})
plt.grid()
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.xlabel(r'Time (ps)', fontsize=18)
plt.ylabel(r'Energy (eV)', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(-100,10000)
plt.ylim(0,50)
plt.savefig(f'k-dt={dt}.png')



##Potential and Total
plt.figure(figsize=(10,9))
t = len(d[:,0])
n_points = t/10
dt = 0.001
plt.plot(d[:,1], label = 'Potential Energy' , color='red')
plt.plot(d[:,2], label = 'Total Energy' , color = 'green')
plt.legend(prop={"size":20})
plt.grid()
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.xlabel(r'Time (ps)', fontsize=18)
plt.ylabel(r'Energy (eV)', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(-100,10000)
plt.ylim(-850,-800)
plt.savefig(f'e-p-dt={dt}.png')



#calculating the average temperature
kinE_average = np.average(d[10000:,0])
k_b = 8.61733034*10**-5
N = 256
T = (2/(3*N -3 ))*(kinE_average)/(k_b)
print(f"average temperature is : {T}")
print(f'avg Pot: {np.average(d[10000:,1])}, std: {np.std(d[10000:,1])}')
print(f'avg Kin: {np.average(d[10000:,0])}, std: {np.std(d[10000:,0])}')
print(f'avg E: {np.average(d[10000:,2])}, std: {np.std(d[10000:,2])}')


#calculating heat capacity
kinE = d[10000:,0]
kinE_average = np.average(kinE)
kinE_2 = (kinE)**2
kinE_2_avg = np.average(kinE_2)
fluc = kinE_2_avg - kinE_average**2
cv = (3/2*N*k_b)/(1-(2/(3*N*k_b**2*(973.15**2))*fluc))
print(f'C_v = {cv}')



#Plotting instantaneous pressure
plt.figure(figsize=(10,9))
pressure = d[:,3]
x = np.ones((len(d[:,4])))
plt.plot(pressure)
plt.ylabel(r'Pressure (GPa)', fontsize=18)
plt.xlabel('Time (ps)', fontsize=18)
t = len(d[:,4])
n_points = t/10
dt = 0.001
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.grid()
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(0,10000)
plt.ylim(-1,4)
plt.plot(x*0.0001, color = 'red' , label='P = 1 bar')
plt.legend(prop={"size":20})
plt.savefig('pressure.png')


#calculating the average temperature
avg_pressure = np.average(d[10000:,3])
print(avg_pressure)



#Plotting instantaneous temperature
plt.figure(figsize=(10,9))
x = np.ones((len(d[:,4])))
temperature = d[:,4] 
plt.plot(temperature)
plt.plot(x*773.15, color = 'red' , label='T = 773.15 K')
plt.ylabel(r'Temperature (K)')
plt.xlabel('Time (ps)', fontsize=18)
t = len(d[:,4])
n_points = t/10
dt = 0.001
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.grid()
plt.legend(prop={"size":20})
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(0,10000)
plt.ylim(650,1400)
plt.savefig('temp.png')



#Plotting lattice constant
plt.figure(figsize=(10,9))
x = np.ones((len(d[:,5])))
a = d[:10000,5] 
plt.plot(a/4)
plt.ylabel(r'Lattice constant ($\AA$)' , fontsize=18)
plt.xlabel('Time (ps)', fontsize=18)
t = len(d[:,4])
n_points = t/10
dt = 0.001
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.grid()
plt.legend(prop={"size":20})
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(0,10000)

plt.savefig('lattice.png')
print(f'average constant: {np.average(a/4)}')




#plotting check positions of 5 selected atoms
plt.figure(figsize=(10,9))
pos = np.loadtxt('positions.txt')
plt.plot(pos[:,0], label = 'atom 1')
plt.plot(pos[:,1], label = 'atom 50')
plt.plot(pos[:,2], label = 'atom 100')
plt.plot(pos[:,3], label = 'atom 150')
plt.plot(pos[:,4], label = 'atom 200')
plt.legend(prop={"size":20})
plt.grid()
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.xlabel(r'Time (ps)', fontsize=18)
plt.ylabel(r'X coordinate ($\AA$)', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(0,10000)

plt.savefig('positions.png')



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
















