# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:09:56 2020

@author: rodri
"""

#Forces
Fp0 = 100 #N
Fp11 = 100  #N
Fp12 = 100  #N
Fp21 = 100  #N
Fp22 = 100  #N
FA1 = 0
FA2 = 0


#Dimensions
lp0 = 0.1  #m
xp1 = 0.3  #m
xcg = 0.53 #m
xp2 = 0.8
xp1 = 0.2  #m

#General parameters
S = 0.3 #m^2
c = 1   #chord [m]
rho = 1.225 #[kg/m^3]
V = 80    #m/s


#aero parameters
xac = 0.6 #m
CL = 1.2  #[-]
Cmac = 0.9 #[-]


Cm = -Fp0*lp0/0.5/rho/V**2/S/c + Fp11*(xcg-xp1)/0.5/rho/V**2/S/c + Fp12*(xcg-xp1)/0.5/rho/V**2/S/c - CL*(xac-xcg)/c - Fp21*(xp2-xcg)/0.5/rho/V**2/S/c -  Fp22*(xp2-xcg)/0.5/rho/V**2/S/c                             

print(Cm)


#Now suppose we increase the angle of attack by a small amount: dalpha translates with equal sign into dCL

dCL = 0.4
CLnew = CL+dCL

Cmnew = -Fp0*lp0/0.5/rho/V**2/S/c + Fp11*(xcg-xp1)/0.5/rho/V**2/S/c + Fp12*(xcg-xp1)/0.5/rho/V**2/S/c - CLnew*(xac-xcg)/c - Fp21*(xp2-xcg)/0.5/rho/V**2/S/c -  Fp22*(xp2-xcg)/0.5/rho/V**2/S/c

dCm = Cmnew-Cm

Cma = dCm/dCL


print(Cma)      #if Cma is negative, it is longitudinally stable