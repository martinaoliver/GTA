#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize

am1_data = np.genfromtxt('Am1_L.txt')
am2_data = np.genfromtxt('Am2_L.txt')
am3_data = np.genfromtxt('Am3_L.txt')

x1 = am1_data[:,0] # conc
y1 = am1_data[:,1] # response
x2 = am2_data[:,0] # conc
y2 = am2_data[:,1] # response
x3 = am3_data[:,0] # conc
y3 = am3_data[:,1] # response

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x1,y1,c='red',label='am1')
ax.scatter(x2,y2,c='blue',label='am2')
ax.scatter(x3,y3,c='green',label='am3')
ax.legend()
plt.show()

logfig = plt.figure()
logax = logfig.add_subplot(1, 1, 1)
logax.set_xscale('log')
logax.scatter(x1,y1,c='red',label='am1')
logax.scatter(x2,y2,c='blue',label='am2')
logax.scatter(x3,y3,c='green',label='am3')
logax.set_xlabel('Ligand Concentration (M)')
logax.set_ylabel('Activity')
logax.legend()
plt.show()

def predict_activity(L,x):
    """ Given ligand concentrations L, and parameters x, predict activities A"""
    a,N,E,Koff,Kon = x
    A = np.divide(a, (1+ np.exp(N* (E + np.log( (1 + np.divide(L,Koff))/(1 + np.divide(L,Kon)))))))
    return A

def loss(x,L,data):
    """squared difference between measured and predicted activity, for an array of data, and parameters x)"""
    diff = np.sum( (predict_activity(L,x)-data)**2)
    return diff

#initial guess
x0_guess=np.array([2,3,-2,0.00005,0.0005])

# minimize provides a unified interface to all of scipy's solvers.
# We'll use the Nelder-Mead solver, we also need to hand it x1 and y1
res = scipy.optimize.minimize(loss, x0_guess, method='Nelder-Mead', args=(x1,y1))
x_fit = res['x'] # fitted parameter values

logfig = plt.figure()
logax = logfig.add_subplot(1, 1, 1)
logax.set_xscale('log')
logax.scatter(x1,y1,c='red',label='am1')
logax.plot(x1, predict_activity(x1,x_fit), label='prediction') # plot predictions from parameters
logax.set_xlabel('Ligand Concentration (M)')
logax.set_ylabel('Activity')
logax.legend()
plt.show()

