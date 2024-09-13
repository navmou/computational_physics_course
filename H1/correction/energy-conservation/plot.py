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
d = np.loadtxt("energies.txt")

#Plotting Energies
##Kinetic 
plt.figure(figsize=(10,9))
t = len(d[:,0])
n_points = t/11
dt = 0.001
plt.plot(d[:,0], label = 'Kinetic Energy')
plt.legend(prop={"size":20})
plt.grid()
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.xlabel(r'Time (ps)', fontsize=18)
plt.ylabel(r'Energy (eV)', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(0,100)
plt.ylim(0,43)
plt.savefig(f'k-dt={dt}.png')



##Potential and Total
plt.figure(figsize=(10,9))
t = len(d[:,0])
n_points = t/11
dt = 0.005
plt.plot(d[:,1], label = 'Potential Energy' , color='red')
plt.plot(d[:,2], label = 'Total Energy' , color = 'green')
plt.legend(prop={"size":20})
plt.grid()
plt.xticks(np.arange(0,t+1,n_points),np.arange(0,t+1,n_points)*dt)
plt.xlabel(r'Time (ps)', fontsize=18)
plt.ylabel(r'Energy (eV)', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlim(0,20)
#plt.ylim(-850,-800)
plt.savefig(f'e-p-dt={dt}.png')



#calculating the average temperature
kinE_average = np.average(d[10000:,0])
k_b = 8.61733034*10**-5
N = 256
T = (2/(3*N -3 ))*(kinE_average)/(k_b)
print(f"average temperature is : {T}")
print(f'avg Pot: {np.average(d[10000:,1])}')
print(f'avg E: {np.average(d[10000:,2])}')


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



#plotting the histogram of N<r>
plt.figure(figsize=(10,9))
pair = np.loadtxt('pair-dist.txt')
plt.hist(pair,100)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=18)
plt.xlabel(r'pair distance ($\AA$)', fontsize=18)
plt.ylabel('number of pairs', fontsize=18)



#calculating the N_ideal 
k = np.linspace(1,53)
#delta_r = 0.5152963499999998
delta_r = 5.1529635
n_ideal = (N-1)/(4*4.04)**3*(4*np.pi/3)*(3*k**2-3*k+1)*delta_r**3

#calculating g(r)
p = plt.hist(pair,normed=True)
n = plt.hist(n_ideal,normed=True)
g = p[1]/n[1]
plt.hist(g)




