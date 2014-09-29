import numpy as np
import matplotlib.pyplot as plt             

T=100.                #Flight Duration
dt=0.1
N=int(T/dt)+1         #No. of Time Steps
t=np.linspace(0,T,N)
                          
ms=50                 #Mass of the rocket
g=9.81                #Gravity  
rho=1.091             #Density of air
r=.5                  #Radius of rocket
A=np.pi*r**2          #Face Area
cd=.15                #Coefficient of Drag
dt=0.1                #Time Step
ve=325                #Initial Exhaust velocity
br=20.                #Propellant Burning Rate
             
pbr=np.zeros(N)
mp=np.zeros(N)
TMa=np.zeros(N)
C1=np.zeros(N)
C2=np.zeros(N)
v=np.zeros(N)

mpo=mp[0]=100.                #Initial Propollant Mass

#Calculating Propellant Burn Rate

pbr[1:5/dt+1]=br              #Defining the Burn rate with respect to time

for n in range (0,N):
     mp[n]=mpo-pbr[n]*dt
     mpo=mp[n]
     TMa[n]=ms+mp[n]
     C1[n]=pbr[n]/TMa[n]
     C2[n]=0.5*rho*A*cd/TMa[n]
     #print n*dt,pbr[n],mp[n],TMa[n],C1[n],C2[n]  
     
# Solving h & v
  
h=np.zeros(N)
V=np.zeros(N)

for n in range(1,N-1):
    
    if h[n]<0:
            h[n]=0
            #v[n]=0
            #print n*dt
            #break
    else:
        h[n+1]=h[n] + dt * (v[n])
        v[n+1]=v[n] + dt * (-g+C1[n]*ve-C2[n]*v[n]*abs(v[n]))
            
        #print n*dt,v[n+1],h[n+1]
        
plt.plot(t,v)
plt.plot(t,h)
plt.show()  

Vmax=max(v)


for i,j in enumerate(v):
    if j==Vmax:
        print "Rocket took ",t[i-1] , "Sec to reach maximum velocity of ", Vmax, "m/s"
        print "Rocket took ",h[i-1] , "Meters of height to reach maximum velocity of ", Vmax, "m/s"
        
Hmax=max(h)

for i,j in enumerate(h):
    if j==Hmax:
        print "Rocket took ",t[i-1], "Sec to reach maximum height of", Hmax
        
for i,j in enumerate(h[3:]):
    
    if j<0.01:
        print "Rocket Hits ground at time ",t[i+2], "Sec"
        print "Rockets velcoity at the time of impact ",(v[i+2]),"m/s"
        break
    else:
        continue
    break