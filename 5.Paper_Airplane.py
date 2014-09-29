# Paper Airplane Trajectory
# Author: Vignesh V.
# Date: 20/Sep/2014

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, ceil
#   INPUTS

g        =    9.8
vt       =    4.9
cd       =    1./5
cl       =    1.

v0       =    6.5
theta0   =    -0.1
x0       =    0.
y0       =    2.

#   DECLARATIONS
dt       = 0.01
    
T      = 20.
N      = int(T/dt)+1

u_e      = np.zeros((N,4))
u_r      = np.zeros((N,4))
u_e[0]   = np.array([v0,theta0,x0,y0])
u_r[0]   = np.array([v0,theta0,x0,y0])

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
    u_rk = u + 0.5 * dt * f(u)
    return u + dt * f(u_rk)
    
def euler(u,f,dt):
    
    return u + dt*f(u)
    
for n in range(N-1):
    
    u_e[n+1]=euler(u_e[n],f,dt)
    u_r[n+1]=runge(u_r[n],f,dt)
    if u_e[n+1,3]<=0.:
        
        break
    if u_r[n+1,3]<=0.:
        break
                  
x_e=u_e[:,2]
y_e=u_e[:,3]

x_r=u_r[:,2]
y_r=u_r[:,3]
    
plt.figure(figsize=(8,6))
plt.grid(True)
plt.xlabel(r'x', fontsize=18)
plt.ylabel(r'y', fontsize=18)
plt.title('Paper Airplane trajectory, flight time = %.2f' % T, fontsize=18)
plt.plot(x_e,y_e, 'b-', lw=2);
plt.plot(x_r,y_r, 'r--', lw=2);
plt.show()   
