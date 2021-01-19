#!/usr/bin/python3

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


# Question 1
# this imports as a pandas data frame, which is (loosely) like numpy array with
# labels for the rows and columns
csheet = pd.read_excel("Epithelia_polygon_data.xls", sheet_name="Control")
msheet = pd.read_excel("Epithelia_polygon_data.xls", sheet_name="Mutant")

print(csheet)
print(msheet)

# Question 2
C1 = csheet[0:7]["n"]  # vector of polygon classes
C2 = csheet[0:7][[1, 2, 3]]  # matrix frequencies of polygon classes

mc = np.mean(C2, 1)  # mean frequency of each polygon class
sc = np.std(C2, 1, ddof=1)  # ddof means weight by N not N-1 (like matlab std(C2,1,2)

# use in jupyter notebooks
#%matplotlib inline

plt.style.use("ggplot")
x_pos = [i for i, _ in enumerate(mc)]

plt.bar(C1, mc, color="red", yerr=sc, align="center", ecolor="black", linewidth=2.0, capsize=3)

plt.xlabel("Polygon Class n")
plt.ylabel("Control")
plt.grid(False)
plt.show()

# Mutant data
C1m = msheet[0:7]["n"]  # vector of polygon classes
C2m = msheet[0:7][[1, 2, 3]]  # matrix frequencies of polygon classes

meanmut = np.mean(C2m, 1)  # mean frequency of each polygon class
stdmut = np.std(C2m, 1, ddof=1)  # ddof means weight by N not N-1 (like matlab std(C2,1,2)

# use in jupyter notebooks
#%matplotlib inline

plt.style.use("ggplot")
x_pos = [i for i, _ in enumerate(stdmut)]
plt.bar(C1m, meanmut, color="blue", yerr=sc, align="center", ecolor="black", linewidth=2.0, capsize=3)

plt.xlabel("Polygon Class n")
plt.ylabel("Control")
plt.grid(False)
plt.show()
