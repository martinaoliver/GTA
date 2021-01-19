#!/usr/bin/python3

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def vdp(t,y):
    """calculate Van Der Pol Derivatives"""
    # y is a tuple (y0,y1)
    y0dot = y[1]
    y1dot = (1-y[0]**2)*y[1]-y[0]
    dydt = ( y0dot, y1dot )
    return dydt

solution = scipy.integrate.solve_ivp(vdp, t_span=(0,20), y0=(0,2), method='RK45', rtol=1e-6)

t = solution.t
y0 = solution.y[0]
y1 = solution.y[1]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, y0, color='tab:blue', label='y1')
ax.plot(t, y1, color='tab:orange', label='y2')
ax.set_title('Solution of the van der Pol equation, mu=1')
ax.set_xlabel('time')
ax.set_ylabel('solution')
ax.legend()
plt.show()
