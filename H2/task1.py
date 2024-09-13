#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 11:47:26 2020

@author: navid
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


x = 



mpl.rcParams['figure.titlesize'] = 25 
mpl.rcParams['lines.linewidth'] = 1.5
mpl.rcParams['axes.labelsize'] = 22 
mpl.rcParams['xtick.labelsize'] = 22 
mpl.rcParams['ytick.labelsize'] = 22 
mpl.rcParams['legend.fontsize'] = 22

N = 1
delta_E = -0.436 - 0.113 -(2*-0.294)
E_0 = 2*N*(-.0436 - .0113 - .0294)

T_ = np.arange(0,1500)
k_b = 8.61733034*10**-5

P_ = np.linspace(0,0.99999,1000)

P_T = []

for T in T_:
    F_ = []
    for P in P_:  
        x = E_0 - 2*N*P*P*delta_E - 2*N*k_b*T*np.log(2) + N*k_b*T*((1-P)*np.log(1-P)+(1+P)*np.log(1+P))
        F_.append((x , P))
    
    F_ = np.array(F_)
    P_T.append(F_[np.argmin(F_[:,0]),1])
    




#plotting P(T)
plt.figure(figsize=(15,10))
plt.plot(P_T,'o' , label='Numerical simulation')

plt.xlabel(r'$T$ (K)')
plt.ylabel('P(T)')


plt.plot(np.ones(500)*905.15,np.linspace(0,1,500) , 'r--', label=r'Theory prediction ($T_c$=905.15K)')
plt.xticks(list(plt.xticks()[0]) + [906])
plt.legend(prop={'size':20})
plt.xlim(0,1500)
plt.savefig('transition.png', dpi=100)


#plotting U(T)
plt.figure(figsize=(15,10))
U = []
for P in P_T:
    U.append((E_0 - (2*P*P*delta_E))/N)

plt.plot(U,'o' , label ='Numerical simulation')

plt.plot(np.ones(500)*905.15,np.linspace(-0.2490,-0.16859,500) , 'r--', label=r'Theory prediction ($T_c$=905.15K)')
plt.xticks(list(plt.xticks()[0]) + [906])
plt.xlabel(r'$T$ (K)')
plt.ylabel(r'$U/N(eV)$')
plt.legend(prop={'size':20})
plt.xlim(0,1500)
#plt.ylim(-1686.0008,-1686.000+0.00005)
plt.savefig('u.png',dpi=100)




p_t = []
for i in range(250):
    p_t.append(P_T[6*i])


#Plotting C_V
dP = []

for i in range(250-1):
    dP.append((p_t[i+1]-p_t[i])/6)

C = []
for i in range(len(dP)):
    C.append(-4*delta_E*dP[i])

plt.figure(figsize=(15,10))
plt.plot(np.array(C)/10,'o--',markeredgecolor='lightgreen' , color = 'green',markerfacecolor='None')
plt.xlabel(r'$T$(K)')
plt.ylabel(r'$C_{V}/N (eV/K)$')    
plt.tick_params(axis='both', which='major')
plt.tick_params(axis='both', which='minor')
plt.xticks(np.arange(0,251,50),np.arange(0,251,50)*6)
#plt.xticks(list(plt.xticks()[0]) + [])
plt.xlim(0,250)
plt.savefig('cv.png',dpi=100)

# =============================================================================
# 
# #Plotting C_V
# dP = []
# 
# for i in range(500-1):
#     dP.append((P_T[i+1]-P_T[i])/0.3)
# 
# C = []
# for i in range(len(dP)):
#     C.append(-4*delta_E*dP[i])
#     
# plt.plot(C)
#     
# =============================================================================





#TASK2 PLOTTING



for temp in range(0,1000 , 50):
    d = np.loadtxt(f'Temp_{temp}.txt')
    plt.figure(figsize=(15,10))
    plt.plot(d[:,3], label = f'T = {temp}')
    plt.ylabel('Energy (eV)')
    plt.xlabel('Time')
    plt.legend()
    plt.savefig(f'equilibration-temp{temp}.png',dpi = 100)
    


E = []
for temp in range(0,1300 , 50):
    d = np.loadtxt(f'Temp_{temp}_EQ.txt')
    E.append(np.average(d[:,3]))

plt.figure(figsize=(15,10))
plt.plot(E)
plt.ylabel('Energy (eV)')
plt.xlabel('Temperature (K)')
plt.xticks(np.arange(0, len(E), 2) , np.arange(0 ,len(E),2)*50)
plt.grid()

plt.savefig(f'E(T).png',dpi = 100)

with open('E_T.txt' , 'w') as f:
    for i in E:
        f.write(f'{i}\n')
        





N_aa = []
N_bb = []
N_ab = []

for temp in range(0,1300 , 50):
    d = np.loadtxt(f'Temp_{temp}_EQ.txt')
    E.append(np.average(d[:,3]))







E_0 = 4000*(-.0436 - .0113 - .0294)

plt.plot(d)


plt.plot(d[:,0] , label=r'$N_aa$')
plt.plot(d[:,1] , label=r'$N_bb$')
plt.plot(d[:,2] , label=r'$N_ab$')
plt.legend()





#Plotting E(T)
d = np.loadtxt('data/average_values.txt')
E=(d[:,0])



error = sigma/np.sqrt(1000000/1232)


plt.figure(figsize=(15,10))
plt.errorbar(T , E, yerr=error, uplims=True, lolims=True )
plt.ylabel('Energy (eV)')
plt.xlabel('Temperature (K)')
plt.grid()
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.savefig('E_T.png', dpi = 100)



#Calculation and plotting of C(T)
E_sq = d[:,1]

T = np.arange(0,1500,50)
C = []
sigma = []
for i in range(len(T)):
    C.append((E_sq[i] - (E[i]*E[i]))/(k_b*T[i]*T[i]))
    sigma.append(np.sqrt(E_sq[i] - (E[i]*E[i])))
 
 
plt.figure(figsize=(17,13))
plt.plot(T , C ,'.--' )
plt.xlabel('Temperature (K)')
plt.ylabel('C(T) (eV/K)')
plt.plot(np.ones(50)*750 ,  np.linspace(-0.005,C[15]) , 'r--')
plt.xticks(list(plt.xticks()[0]) + [750] , rotation = 90)
plt.xlim(0,1500)
plt.ylim(-0.005,0.35)
plt.grid()

plt.savefig('C_T.png', dpi = 100)




#Plotting long range correlation P(T) 
N = 1000
P = []
n = d[:,2]
for i in range(len(T)):
    P.append((2*n[i]/N)-1)

plt.figure(figsize=(17,13))
plt.plot(T,P, '.--')
plt.xlabel('Temperature (K)')
plt.ylabel('P(T)')
plt.plot(np.zeros(1500) , 'r--')
plt.grid()

plt.savefig('P_T.png', dpi = 100)




#Plotting short range correlation r(T)
N = 1000
r = []
N_ab = d[:,5]
for i in range(len(T)):
    r.append((N_ab[i]-4*N)/(4*N))

plt.figure(figsize=(17,13))
plt.plot(T,r, '.--')
plt.xlabel('Temperature (K)')
plt.ylabel('r(T)')
plt.grid()

plt.savefig('r_T.png', dpi = 100)











for temp in range(0,1500,50):
    b = np.loadtxt(f'data/Temp_{temp}_EQ.txt')
    with open(f'ener{temp}.txt' , 'w') as fuc:
        for i in b[:,3]:
            fuc.write(f'{i}\n')
    with open(f'nab_{temp}.txt' , 'w') as fuc:
        for i in b[:,2]:
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


































sigma_T_Nab = []

for temp in range(0,1501,50):
    lmn = np.loadtxt(f'data/Temp_{temp}_EQ.txt')
    E = lmn[:,2]
    print(np.std(E))
    print(np.mean(E))
    print(np.mean(np.square(E)))
    b = np.mean(np.square(E)) - np.mean(E)**2
    b
    sigma_T_Nab.append(np.sqrt(b))




with open("sigma_T_Nab.txt" , "w") as fp:
    for i in sigma_T_Nab:
        fp.write(f'{i}\n')

















