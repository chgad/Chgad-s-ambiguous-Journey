


import numpy as np
import matplotlib.pyplot as plt
from math import exp




delta= 1.0
sigma =1.0
L =10.0
v= 1.0

x= np.arange(0,10,0.01)


def f(u):
    return delta * exp(-pow((u-0.5*L),2.0)  /  (2.0*pow(sigma,2.0))) - exp(-pow(0.5*L,2.0)  /  (2.0*pow(sigma,2.0)))

def g(u):
    return 0.0

def z_plus(u):
    if(u<=-L):
        return z_plus(u+2.0*L)
    if (u>= -L and u<=0.0):
        return 0.5* (-f(-u) +g(-u)  /  v)
    if (u>=0.0 and u<= L):
        return 0.5*(+f(+u) + g(u)/v)
    if (u>=L):
        return z_plus(u-2.0*L)

def z(x,t):
    return z_plus(+x+v*t)-z_plus(-x + v*t)

v_z=np.vectorize(z)

plt.figure(1)

for t in range(0,9):
    p=plt.subplot(3,3,t+1)
    plt.plot(x,v_z(x,t))
    plt.ylabel("z(t,x)")
    plt.title("t=%s" % t)
    p.set_xlim([0,10])
    p.set_ylim([-1,1])

plt.tight_layout()

plt.show()