#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab6
"""
This code plots water temperatures

Yesh 3/25/2020
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def toC(x):
    temp = x[-1]
    y = list(x)
    y[-1] = (temp - 32)*(5/9)
    x = tuple(y)
    return x

def convertToC(file):
    for i in range(0, len(file)):
        temp = file[i][-1]
        file[i][-1] = (temp - 32)*(5/9)

dtype1 = np.dtype([('Agency', 'U100'),('Station ID', 'U100'), ('Year-Month-Day', 'U100')
, ('Time', 'U100'), ('Eastern Daylight time', 'U100')
, ('Water Temp', 'f8')])

fname1 = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab6\\Colrain.dat';
fname2 = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab6\\North.dat';

temp_dataG = np.loadtxt(fname1, dtype=dtype1, skiprows=30, delimiter = ',' , usecols=(0,1,2,3,4,5))
temp_dataN = np.loadtxt(fname2, dtype=dtype1, skiprows=28, delimiter = ',' , usecols=(0,1,2,3,4,5))


vfunc = np.vectorize(toC)
temp_dataG = vfunc(temp_dataG)
temp_dataN = vfunc(temp_dataN)

plt.plot(temp_dataG[-1])
plt.plot(temp_dataN[-1])

