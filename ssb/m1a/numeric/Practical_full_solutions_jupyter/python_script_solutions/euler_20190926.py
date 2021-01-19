#!/usr/bin/python


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate

#Example Euler's method

#parameters
a=3
b=1
c=4
d=1
#initial conditions
m0=100
P0=0
varm = 2*a
varP = 2*a*c/b

npoints = 100 # number iterations time = npoints*dt
dt=0.1
m = np.zeros(npoints)
P = np.zeros(npoints)
t = np.zeros(npoints)

# initial conditions
m[0]= m0
P[0]= P0
t[0] = 0.0

for step in range(npoints-1):
    # Euler method ym+1 = ym+ dt*f(ym)
    m[step+1] = m[step] + dt*(a-b*m[step]+ np.random.normal(scale=varm))
    P[step+1] = P[step] + dt*( c*m[step] - d*P[step] + np.random.normal(scale=varP))
    t[step+1] = t[step] + dt          

   
# plot(t,m,'r',t,P,'b'); %plots the numerical solution for m in red
#                        %and P in blue
                       
# hold on %keep the previously plotted lines

def  dydt_lange(t,y):
    a = 3 # parameters
    b = 1
    c = 4
    d = 1
    dydt= (a- b *y[0]  , c * y[0]- d *y[1] );
    return dydt

solution = scipy.integrate.solve_ivp(dydt_lange, t_span=(0,10),y0=(m0,P0), method='RK45')
t_ode45 = solution.t
m_ode45 = solution.y[0]
P_ode45 = solution.y[1]


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, m, color='tab:blue',label='m(t) rand')
ax.plot(t, P, color='tab:orange',label='P(t) rand')
ax.set_title('Euler with noise and OD45 solutions')
ax.set_xlabel('time')
ax.set_ylabel('concentrations')

ax.plot(t_ode45, m_ode45, color='tab:red',label='m(t) det')
ax.plot(t_ode45, P_ode45, color='tab:green',label='P(t) det')
ax.legend()
plt.show()
