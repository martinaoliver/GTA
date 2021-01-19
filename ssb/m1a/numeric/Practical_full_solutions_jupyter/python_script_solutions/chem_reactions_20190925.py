#!/usr/bin/python

import numpy as np
import scipy.integrate
from timeit import default_timer as timer
import matplotlib.pyplot as plt
%matplotlib inline

def main():
    k1=0.1
    k2=0.3
    A0,B0=1,0
    dydt_withks = lambda t,y: dydt(t,y,k1,k2)
    
    start = timer()
    solution = scipy.integrate.solve_ivp(dydt_withks, t_span=(0,10),y0=(A0,B0), method='RK45')
    end = timer()
    time_for_num_int_by_ode45= end-start
    print("time for ODE45, ",   time_for_num_int_by_ode45)
    
    t_ode45 = solution.t
    A_ode45 = solution.y[0]
    B_ode45 = solution.y[1]
    print("Equilibrium points of A, B")
    print(A_ode45[-1],B_ode45[-1])
    
    start = timer()
    solution = euler(dydt, (0,10),np.array([A0,B0]),k1,k2)
    end = timer()
    time_for_num_int_by_euler= end-start
    print("time for Euler, ",   time_for_num_int_by_euler)
    t_euler = solution[0]
    A_euler = [A for (A,B) in solution[1]]
    B_euler = [B for (A,B) in solution[1]]
    
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t_ode45, (A_ode45), color='tab:blue',label='A(t)')
    ax.plot(t_ode45, (B_ode45), color='tab:orange',label='B(t)')
    ax.set_title('OD45 solution')
    ax.set_xlabel('time')
    ax.set_ylabel('solution')
    ax.legend() 

    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t_euler, (A_euler), color='tab:blue',label='A(t)')
    ax.plot(t_euler, (B_euler), color='tab:orange',label='B(t)')
    ax.set_title('Euler solution')
    ax.set_xlabel('time')
    ax.set_ylabel('solution')
    ax.legend() 

    plt.show()



    
def dydt(t,y,k1,k2):

    A, B= y
    dAdt = -2*k1*A**2 + 2*k2*B 
    dBdt =  k1*A**2-k2*B
    return (dAdt, dBdt)


def euler(dydt,time_interval,y0,k1,k2):

    Y= [y0]
    dt = 0.001 # integration step
    t_start = time_interval[0]
    t_max= time_interval[1]
    T = [t_start]
    while t_start <= t_max:
        Y.append( Y[-1] + np.multiply(dt,dydt(t_start, Y[-1],k1,k2)))
        t_start = t_start + dt
        T.append(t_start)

    return (T,Y)

   
if __name__ == "__main__":
    main()
