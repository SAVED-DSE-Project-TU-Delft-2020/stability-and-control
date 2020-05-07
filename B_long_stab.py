# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:52:17 2020

@author: rodri

Horizontal distance starts from the nose. Moments defined positive clockwise\

    2 is the wing above
    1 is the wing below
#formula assumes xcg>xac2
#formula assumes lcg >lp1
"""
#Forces
Fp11 = 100  #N
Fp12 = 100  #N
Fp21 = 100  #N
Fp22 = 100  #N

FA11 = 0
FA12 = 0
FA21 = 0
FA22 = 0


#Dimensions
lp1 = 0.2  #m
lp2 = 0.8
lcg = 0.4

xcg = 0.7 #m




XA1 = 1.3
XA2 = 1.3

#General parameters
S1 = 0.3 #m^2
S2 = 0.3 #m^2
c1 = 1   #chord [m]
c2 = 1   #chord [m]
rho = 1.225 #[kg/m^3]
V = 80    #m/s

c = c1 = c2
#aero parameters
xac1 = 0.3
xac2 = 0.5
CL1 = 1.2  #[-]
CL2 = 1.2  #[-]
Cmac1 = 0.9 #[-]
Cmac2 = 0.9 #[-]


Cm = Fp11*(lcg-lp1)/0.5/rho/V**2/S1/c + Fp12*(lcg-lp1)/0.5/rho/V**2/S1/c + CL1*(xcg-xac1)/c + Cmac1 - FA11*(XA1 - xcg)/0.5/rho/V**2/S1/c - FA12*(XA1 - xcg)/0.5/rho/V**2/S1/c - Fp21*(lp2-lcg)/0.5/rho/V**2/S2/c - Fp22*(lp2-lcg)/0.5/rho/V**2/S2/c + CL2*(xcg-xac2)/c + Cmac2 - FA21*(XA2-xcg)/0.5/rho/V**2/S2/c - FA22*(XA2-xcg)/0.5/rho/V**2/S2/c                                                           

#Now suppose we increase the angle of attack by a small amount: dalpha translates with equal sign into dCL

dCL = 0.1
CL1new = CL1 +dCL
CL2new = CL2 +dCL


Cmnew = Fp11*(lcg-lp1)/0.5/rho/V**2/S1/c + Fp12*(lcg-lp1)/0.5/rho/V**2/S1/c + CL1new*(xcg-xac1)/c + Cmac1 - FA11*(XA1 - xcg)/0.5/rho/V**2/S1/c - FA12*(XA1 - xcg)/0.5/rho/V**2/S1/c - Fp21*(lp2-lcg)/0.5/rho/V**2/S2/c - Fp22*(lp2-lcg)/0.5/rho/V**2/S2/c + CL2new*(xcg-xac2)/c + Cmac2 - FA21*(XA2-xcg)/0.5/rho/V**2/S2/c - FA22*(XA2-xcg)/0.5/rho/V**2/S2/c                                                           


dCm = Cmnew-Cm

Cma = dCm/dCL


print(Cma)      #if Cma is negative, it is longitudinally stable