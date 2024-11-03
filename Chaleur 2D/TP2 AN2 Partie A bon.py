from math import exp 
import math
from math import cos,sin,factorial
import matplotlib.pyplot as plt 
import numpy as np
import scipy as sp
# from mpl_toolkits.mplot3d import Axes3d
from scipy.optimize import minimize_scalar
from numpy import linalg as LA
from scipy.linalg import hilbert
from matplotlib import cm
import matplotlib.ticker

####################################

m=20
p=20
cfl=0.45
T=0.01

deltax=1/(m+1)
deltay=1/(p+1)
deltat=cfl*((deltax**2)*(deltay**2))/(2*(deltay**2)+(deltax**2))

lambdax=deltat/deltax**2
lambday=deltat/deltay**2

x=np.linspace(0,1,m)
y=np.linspace(0,1,p)

U0=np.zeros((m,p))
for i in range(m):
    for j in range(p):
        if (x[i]>=0.4) and (x[i]<=0.6) and (y[j]>=0.4) and (y[j]<=0.6):
            U0[i,j]=1

U01=np.zeros((m,p))
t=0
while(t<T):
    if (t+deltat>T):
        deltat=T-t
        lambdax=deltat/deltax**2
        lambday=deltat/deltay**2
        for i in range(m-1):
            for j in range(p-1):
                U01[i,j]=(1-2*(lambdax+lambday))*U0[i,j]+lambdax*U0[i+1,j]+lambdax*U0[i-1,j]+lambday*U0[i,j-1]+lambday*U0[i,j+1]
        U0=U01
    
    for i in range(m-1):
        for j in range(p-1):
            U01[i,j]=(1-2*(lambdax+lambday))*U0[i,j]+lambdax*U0[i+1,j]+lambdax*U0[i-1,j]+lambday*U0[i,j-1]+lambday*U0[i,j+1]
    U0=U01
    t+=deltat

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x,y=np.meshgrid(x,y)
surf = ax.plot_surface(x, y, U0, cmap=cm.coolwarm,linewidth=0, antialiased=False)

#Customize the z-axis

ax.set_major_locator(matplotlib.ticker.LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()