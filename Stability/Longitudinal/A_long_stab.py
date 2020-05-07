# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:33:40 2020

@author: rodri

Horizontal distance starts from the nose. Moments defined positive clockwise
"""
#Forces
Fp1 = 100  #N
Fp2 = 100  #N

FA1 = 0
FA2 = 0


#Dimensions
lp = 0.2  #m
xp = 0.02  #m
xcg = 0.7 #m
XA = 1.3

#General parameters
S = 0.3 #m^2
c = 1   #chord [m]
rho = 1.225 #[kg/m^3]
V = 80    #m/s


#aero parameters
xac = 0.8 #m
CL = 1.2  #[-]
Cmac = 0.9 #[-]


Cm = -Fp1*lp/0.5/rho/V**2/S/c -Fp2*lp/0.5/rho/V**2/S/c - CL*(xac-xcg)/c + Cmac - FA1*(XA-xcg)/0.5/rho/V**2/S/c - FA2*(XA-xcg)/0.5/rho/V**2/S/c

print(Cm)


#Now suppose we increase the angle of attack by a small amount: dalpha translates with equal sign into dCL

dCL = 0.1
CLnew = CL+dCL

Cmnew = -Fp1*lp/0.5/rho/V**2/S/c -Fp2*lp/0.5/rho/V**2/S/c - CLnew*(xac-xcg)/c + Cmac - FA1*(XA-xcg)/0.5/rho/V**2/S/c - FA2*(XA-xcg)/0.5/rho/V**2/S/c

dCm = Cmnew-Cm

Cma = dCm/dCL


print(Cma)      #if Cma is negative, it is longitudinally stable

