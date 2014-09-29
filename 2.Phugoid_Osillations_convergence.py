# Phugoid Oscillations with Convergence and error.

import numpy as np
import matplotlib.pyplot as plt

T = 100.0

dt_val=np.array([0.1,0.05,0.01,0.005,0.001,0.0001])
z_val=np.empty_like(dt_val,dtype=np.ndarray)


for i, dt in enumerate (dt_val):
    
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
    z_val[i]=z.copy()

er_val=np.empty_like(dt_val)

def get_er(z,dt):
    N=len(z)
    t=np.linspace(0,T,N)
    z_exact = v*(zt/g)**.5*np.sin((g/zt)**.5*t)+(z0-zt)*np.cos((g/zt)**.5*t)+zt
    
    return dt*np.sum(np.abs(z_exact-z))
    
for i, dt in enumerate (dt_val):
    er_val[i]=get_er(z_val[i],dt)
    
plt.figure(figsize=(10,6))
plt.tick_params(axis='both', labelsize=14)
plt.grid(True)
plt.xlabel('Delta T',fontsize=14)
plt.ylabel('Error',fontsize=14)

plt.loglog(dt_val,er_val,'ko-')

plt.show()