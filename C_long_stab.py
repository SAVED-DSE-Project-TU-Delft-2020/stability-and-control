# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:38:35 2020

@author: rodri
"""

#Forces

Fpo = 100
Fp11 = 100
Fp12 = 100
Fp21 = 100
Fp22 = 100



V = 100
S = 2
rho = 1.225
c = 1
#distances

xp0 = -0.1
xp1 = 0.1
xp2 = 0.6

xac = 0.3
xcg = 0.4

#xnp = xac + CL_a_h/CL_a_Ah*(1- de/da)*Sh*lh/S*c*(Vh/V)**2

xnp = 0.5

xh = 1.2


lp0 = 0.1
lp1 = 0.1
lp2 = 0.2



CLw = 1.2
CLh = 0.2
Cmacw = 0.1
Cmach = 0.35
dCL = 0 # no disturbance yet




Cm = -Fpo*lp0/0.5/rho/V**2/S/c + -Fp11*(xcg-xp1)/0.5/rho/V**2/S/c -Fp12*(xcg-xp1)/0.5/rho/V**2/S/c + CLw*(xcg-xac)/c -dCL*(xnp-xcg)/c - Fp21*(xp2-xcg)/0.5/rho/V**2/S/c  - Fp22*(xp2-xcg)/0.5/rho/V**2/S/c  - CLh*(xh-xcg)/c + Cmacw + Cmach                                    


#add disturbance

dCL = 0.2
Cmnew = -Fpo*lp0/0.5/rho/V**2/S/c + -Fp11*(xcg-xp1)/0.5/rho/V**2/S/c -Fp12*(xcg-xp1)/0.5/rho/V**2/S/c + CLw*(xcg-xac)/c -dCL*(xnp-xcg)/c - Fp21*(xp2-xcg)/0.5/rho/V**2/S/c  - Fp22*(xp2-xcg)/0.5/rho/V**2/S/c  - CLh*(xh-xcg)/c + Cmacw + Cmach

dCm = Cmnew-Cm

Cma = dCm/dCL


print(Cma)      #if Cma is negative, it is longitudinally stable





