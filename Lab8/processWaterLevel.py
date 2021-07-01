# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:23:12 2020

@author: yeshw
"""

import numpy as np
import os
import datetime as dt
import matplotlib.pylab as plt
import matplotlib.dates as mdates
import matplotlib.ticker as plticker
directory = os.path.join("C:\\","Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab8\\Whately\\MFS\\")
alldata = []

path = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab8\\Whately\\MFS'

file = 'MFS1-7-2019.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()

file = 'MFS1-8-2019.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()

file = 'MFS1-9-2019.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()


file = 'MFS1-10-2019.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()


file = 'MFS1-11-2019.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()

file = 'MFS1-12-2019.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()

file = 'MFS1-1-2020.csv'
print("Processing " , file)
dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
alldata = alldata +  data_TEMP.tolist()


#for root,dirs,files in os.walk(directory):
#    for file in files:
#       if file.endswith(".csv"):           
#           print("Processing " , file)
#           dtype1 = np.dtype([('Date', 'U10'),('Time', 'U10'), ('MS', 'f8'), ('Level', 'f8'), ('Temperature', 'f8')])
#           data_TEMP = np.loadtxt(directory + file, dtype=dtype1, skiprows=12, delimiter = ',')
#           alldata = alldata +  data_TEMP.tolist()
           

f = open('alldata.csv','w+')
dates_x = []
water_level_y = []
first_date = dt.datetime.strptime(alldata[0][0],"%m/%d/%Y").date()
for i in alldata:
    dates_x.append(dt.datetime.strptime(i[0],"%m/%d/%Y").date())
    water_level_y.append(i[3] + 24)
    f.write(i[0] +','+ i[1] + 'm' +','+ str(i[2]) + ',' + str(i[3]) + ',' + str(i[4]) + '\n')
f.close()
#print(dates_x)

plt.figure(1)
ax = plt.gca()
formatter = mdates.DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(formatter)
loc = plticker.MultipleLocator(base=10000.0) 
ax.xaxis.set_major_locator(loc)
locator = mdates.DayLocator()
ax.xaxis.set_major_locator(locator)
plt.xticks(np.arange(min(dates_x), max(dates_x), dt.timedelta(40)))
plt.plot(dates_x, water_level_y)
plt.show()

dt = 1/(6*24)
plt.figure(2)
F = np.fft.fft(water_level_y)
plt.xlabel('frequency(cycles/day)')
plt.ylabel('amplitude(V)')
sample_freq = np.fft.fftfreq(len(water_level_y), d = dt)
pixds = np.where(sample_freq >= 0)
freqsAn = sample_freq[pixds]
plt.xlim(0,4.5)
plt.semilogy(freqsAn[pixds],(np.abs(F[pixds])*(2/len(water_level_y))))
plt.legend(loc=2)
plt.show()