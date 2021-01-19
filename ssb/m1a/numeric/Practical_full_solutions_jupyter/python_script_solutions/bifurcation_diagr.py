#!/usr/bin/python3

# solving for 0 derivatives gives two solutions requires c < (1/2)
# where c = ab
# as 4c^2 < 1

import numpy as np
import matplotlib.pyplot as plt

c = np.arange(0.1,0.501,0.01)
p1 = np.divide(1 + np.sqrt( (1-4* np.square(c))),np.multiply(2,c))
p2 = np.divide(1 - np.sqrt( (1-4* np.square(c))),np.multiply(2,c))
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(c, p1, color='tab:blue',label='p1')
ax.plot(c, p2, color='tab:orange',label='p2')
ax.set_title('Bifurcation diagram')
ax.set_xlabel('c')
ax.set_ylabel('[P]')
ax.legend()
plt.show()
