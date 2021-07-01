#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab6
"""
This code plots water temperatures

Yesh 2/26/2020
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convertToC(file):
    for i in range(0, len(file)):
        temp = file[i][-1]
        file[i][-1] = (temp - 32)*(5/9)

def convertToASCII(file):
    for i in range(0, len(file)):
        file[i].encode("utf-8")

dtype1 = np.dtype([('Agency', 'U100'),('Station ID', 'U100'), ('Year-Month-Day', 'U100')
, ('Time', 'U100'), ('Eastern Daylight time', 'U100')
, ('Water Temp', 'f8')])

fname1 = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab6\\Colrain.dat';
fname2 = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab6\\North.dat';

temp_dataG = np.loadtxt(fname1, dtype=dtype1, skiprows=30, delimiter = ',' , usecols=(0,1,2,3,4,5))
temp_dataN = np.loadtxt(fname2, dtype=dtype1, skiprows=28, delimiter = ',' , usecols=(0,1,2,3,4,5))

convertToC(temp_dataG)
convertToC(temp_dataN)

plt.plot(temp_dataG['Water Temp'])
plt.plot(temp_dataN['Water Temp'])

print(temp_dataG)
print(temp_dataN)
