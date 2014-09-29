# Full Phugoid Motion
# Author: Vignesh V.
# Date: 26/Sep/2014

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, ceil
#   INPUTS

g        =    9.8
vt       =    30
cd       =    1./40.
cl       =    1.

v0       =    6.5
theta0   =    -0.1
x0       =    0.
y0       =    2.0
T        =    20.

#   DECLARATIONS

dt_val = ([0.01,0.005,0.001,0.0001])
z_valr  = np.empty_like(dt_val,dtype=np.ndarray)
z_vale  = np.empty_like(dt_val,dtype=np.ndarray)

for i,dt in enumerate (dt_val):
        
    N      = int(T/dt)+1
    u_r      = np.zeros((N,4))
    u_r[0]   = np.array([v0,theta0,x0,y0])
    u_e      = np.zeros((N,4))
    u_e[0]   = np.array([v0,theta0,x0,y0])

    def f(u):
        v=u[0]
        theta=u[1]
        x=u[2]
        y=u[3]
        
        return np.array([-g*sin(theta) - cd/cl*g/vt**2*v**2,
                        -g*(cos(theta)/v-v/vt**2),
                        v*cos(theta),
                        v*sin(theta)])
    
    def runge(u,f,dt):
        u_run = u + 0.5*dt*f(u)
        
        return u + dt*f(u_run)
        
    def euler(u,f,dt):
        
        return u + dt*f(u)
        
    for n in range(N-1):
        
        u_r[n+1]=runge(u_r[n],f,dt)
        if u_r[n+1,3]<0.0:
            break
        
    z_valr[i]=u_r.copy()
    
    for n in range(N-1):
    
        u_e[n+1]=euler(u_e[n],f,dt)
        if u_e[n+1,3]<0.0:
            break
        
    z_vale[i]=u_e.copy()

er_valr=np.empty_like(dt_val)
er_vale=np.empty_like(dt_val)

def get_er(z_c,z_f,dt):
    
    N_Cur=len(z_c[:,0])
    N_Fin=len(z_f[:,0])
    
    g_r=ceil(N_Fin/float(N_Cur))
    
    dif_grd=dt*np.sum(np.abs(z_c[:,2]-z_f[::g_r,2]))
        
    return dif_grd

for i, dt in enumerate(dt_val):
    
    er_valr[i]=get_er(z_valr[i],z_valr[-1],dt)
    er_vale[i]=get_er(z_vale[i],z_vale[-1],dt)

plt.figure(figsize=(10,6))
plt.tick_params('both', labelsize=14)
plt.grid(True)
plt.xlabel('Delta T', fontsize=14)
plt.ylabel('Error', fontsize=14)
plt.loglog(dt_val,er_valr, 'ko-')
plt.loglog(dt_val,er_vale, 'ro-')

plt.show()   
