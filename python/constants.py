import numpy as np
import matplotlib.pyplot as plt

mm=1e-3
gr = 1e-3

D=0.08/1000 #[inch]
h = 249*mm
G = np.asarray([130E9,160E9])
m=20.5*gr
M = 0.0753

l_sides = 105*mm 
l_center = 8*mm
l_sides = np.asarray([l_sides,l_sides]) #  length [mm] 
l = 2*l_sides[0] + l_center #  length [mm] 
l /=2

# l=238*mm/2

kappa = (G*np.pi*D**4)/(h*32)
I_CM = M*((2*l)**2)/12
I1 = 2*m*l**2
# I =np.asarray([I1,I1 + 2*I_CM])
# I = 0.0007853341
T = 2*np.pi*np.sqrt(I/kappa[:,None])

# ACTUAL
T=84
1/((T/(2*np.pi))**2)/I1)




75.3+41


# # brownian uncertainty

# T0 = 300
# k_b = 1.380649e-23
# noise = np.sqrt(k_b*T0/kappa)

# e= 1.6e-19



# VT = k_b*T0/e
# n = 4
# c = n*k_b*T0/e *np.log(10)
# Is = 5e16
# I= np.arange(0,2601)/100000

# vd = c*np.log10(I/Is)

# # rd = (VT/I[-100])
# # Vthersh = 0.71
# # I1=[]
# # for v in vd:
# #     if -v<Vthersh:
# #         I1.append((v+Vthersh)/rd)
# #     # if v>Vthersh:
# #     #     I1.append((v-Vthersh)/rd)
# #     else:
# #           I1.append(0)

# N = 6
# P = I*N*(-vd)
# R = 360
# # vs = (P*R-vd**2)/(-vd)

# vs = (I*R+vd)


# plt.plot(vd,I)
# # plt.plot(vd,I1)

# # plt.plot(vs,I)

# # plt.plot(vs,P)

# # plt.plot(P,I)


# # D = np.arange(2**8)/2**8*100
# # vs = 0.05*D
