#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

a=0.7
b=0.6
c=a*b

p1 = (1+np.sqrt(1-4*c**2))/(2*c)
p2 = (1-np.sqrt(1-4*c**2))/(2*c)


X = np.arange(0,2.5,0.2)
Y = np.arange(0,2.5,0.2)
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html
m , p = np.meshgrid(X,Y)
      
mdot = np.divide(  np.square(p) , (1+np.square(p))) - np.multiply(b,m)
pdot = np.subtract(m, np.multiply(a,p))

fig, ax = plt.subplots()
q=ax.quiver(p,m,pdot,mdot)
ax.quiverkey(q,X=0.3,Y=2.4, U=5,
             label='Quiver key, length = 5', labelpos='E')
ax.plot(p,np.multiply(a,p))
ax.plot(p, np.divide( np.square(p), np.multiply(b,(1+np.square(p)))))
ax.set_xlabel('p')
ax.set_ylabel('m')
ax.set_title('phase portrait')


def dydt_autoactiv(t,y,a,b):

    y1,y2=y
    dy1 = y2**2/(1+y2**2)-b*y1
    dy2 = y1-a*y2
    return (dy1,dy2)

# this is a trick so we can pass parameters a,b into the solver
dydt_params = lambda t,y: dydt_autoactiv(t,y,a,b)

solution1 = scipy.integrate.solve_ivp(dydt_params, t_span=(0,20),y0=(2,2), method='RK45')
t1_ode45 = solution1.t
m1_ode45 = solution1.y[0]
p1_ode45 = solution1.y[1]
ax.plot(p1_ode45,m1_ode45)

solution2 = scipy.integrate.solve_ivp(dydt_params, t_span=(0,20),y0=(0,0.5), method='RK45')
t2_ode45 = solution2.t
m2_ode45 = solution2.y[0]
p2_ode45 = solution2.y[1]
ax.plot(p2_ode45,m2_ode45)
plt.show()


