# Phugoid Oscillations

import numpy as np
import matplotlib.pyplot as plt

T = 100.0
dt = 0.01
N = int(T/dt)+1

t=np.arange(0.0,T+dt,dt)

z0 = 100.
v  = 10 
zt = 100.
g  = 9.81

u = np.array([z0, v])

z = np.zeros(N)
z[0] = z0 

for n in range(1,N):
    u = u + dt*np.array([u[1], g*(1-u[0]/zt)])
    #print u
    z[n] = u[0]

z_exact = v*(zt/g)**.5*np.sin((g/zt)**.5*t)+(z0-zt)*np.cos((g/zt)**.5*t)+zt
            
plt.figure(figsize=(10,4))
plt.ylim(40,160)             #y-axis plot limits
plt.tick_params(axis='both', labelsize=14) #increase font size for ticks
plt.xlabel('t', fontsize=14) #x label
plt.ylabel('z', fontsize=14) #y label
plt.plot(t,z)
plt.plot(t, z_exact)
plt.legend(['Numerical Solution','Analytical Solution']);            

plt.show()