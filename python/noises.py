# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

A = 1.14E-2
P = 1E-2
m_1 = 0.0753


T = 298.0
T_0 = 0
N_A = 6.022E23
R = 8.314
k=1.38e-23


# vacuum chamber volume
(67897.67+44301+362902.18 )*1e-9
V=4.75e-4
RHOE_N = P/(k*T)
# N = P*V/(k*T)
# N/N_A


# mu_298k = 1.85e-5*np.sqrt()
# bolzman
SIGMA = 5.67E-8

eps= np.asarray([0.0919,0.0798,0.0666,0.051,0.0417])
t= np.asarray([300,240,180,120,80])
z= np.polyfit(t,eps,1)
EPSILON =T_0*z[0]+z[1]
c=3e8
p =SIGMA  *EPSILON*A*(T**4-T_0**4)
print('black body',p)
p_RMS =(2.7*A*k)/(c**2*m_1)*(4-3*EPSILON)*SIGMA*T**5
print('black body RMS',p_RMS)

# thermal
C_V = 0.716E3
M =28.9647e-3
m = M/N_A

M/m
p = A*P*C_V*(T-T_0)*np.sqrt(M/(R*T))
print('thermal ',p)



# BROWNIAN

# p = 6/N_A*np.sqrt(P*A*R*T*np.sqrt(3*R*T/M))
# print(p)
p = 36/m_1*(A*P)**2 

# p = 6*A*RHOE_N*k*T*np.sqrt(3*R*T/M)
print('BROWNIAN ',p)
p_RMS = 12*A*P/m_1*np.sqrt(3*k*T*M/N_A)
print('BROWNIAN RMS',p_RMS)

v = np.sqrt(3*R*T/M)

# ACOUSTIC
c=1e-22
p = A*P**2*c
print('ACOUSTIC',p)



T1=299
T0=np.arange(T1*100)/100.0
T = np.ones(T1*100)*298.0





p=SIGMA*(T0*z[0]+z[1])*A*(T**4-T0**4)+np.sqrt(M/(R*T1))*C_V*A*P*(T-T0)

plt.plot(T0,p)



max_tourqe = 6.8e-10
THETA_MAX=1E-6
OMEGA = 2*np.pi/84
p = max_tourqe/2*THETA_MAX*OMEGA 
# # ACOUSTIC
# rho = M*P/(R*T)
# k_s = 142E3
# p = A*P*np.sqrt(k_s/rho)



# eps= np.asarray([0.0919,0.0798,0.0666,0.051,0.0417])
# t= np.asarray([300,240,180,120,80])
# z= np.polyfit(t,eps,1)
# plt.plot(t,eps)
# t1 = np.arange(300)
# plt.plot(t1,t1*z[0]+z[1])

36*(M*k*300/N_A*3)**.25*(P*A)**1.5*12/m_1


# RESOLUTION LIMIT ONE SIDED
theta = 5e-8


r=0.1
T=84
L = 0.218
G=6.67E-11

M = (12*np.pi**2*L)/(G*T**2)*r**2*theta
print(M*1000)