# Full Phugoid Motion
# Author: Vignesh V.
# Date: 15/Sep/2014

import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos
#   INPUTS

g        =    9.8
vt       =    30
cd       =    1./40.
cl       =    1.

v0       =    vt
theta0   =    0.
x0       =    0.
y0       =    1000.

#   DECLARATIONS

dt     = 0.1
T      = 100
N      = int(T/dt)+1

u      = np.zeros((N,4))
u[0]   = np.array([v0,theta0,x0,y0])

def f(u):
    v=u[0]
    theta=u[1]
    x=u[2]
    y=u[3]
    
    return np.array([-g*sin(theta) - cd/cl*g/vt**2*v**2,
                      -g*(cos(theta)/v-v/vt**2),
                       v*cos(theta),
                       v*sin(theta)])
    
def euler(u,f,dt):
    
    return u + dt*f(u)
    
for n in range(N-1):
    
    u[n+1]=euler(u[n],f,dt)
    
x=u[:,2]
y=u[:,3]


plt.figure(figsize=(8,6))
plt.grid(True)
plt.xlabel(r'x', fontsize=18)
plt.ylabel(r'y', fontsize=18)
plt.title('Glider trajectory, flight time = %.2f' % T, fontsize=18)
plt.plot(x,y, 'k-', lw=2);
plt.show()   
