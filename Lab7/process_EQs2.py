#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab6
"""
This code extracts GPS data from an Earth Quake in calfornia and plots the locations

Yesh 3/25/2020
"""

import numpy as np 
import datetime as dt
import time
import matplotlib.pylab as plt
import pandas as pd

northridge_lon = [-118.535]
northridge_lat = [34.207]

dtype1 = np.dtype([('Year', 'i4'),('Month', 'i4'),('Day', 'i4'),('Hour', 'i4')
                   ,('Minute', 'i4'),('Seconds', 'f8'), ('Latitude', 'f8')
                   ,('Longitude', 'f8'),('Magnitude', 'f8'),])

fname1 = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab6\\NorthridgeEQ.dat';

start = time.time()

data = np.loadtxt(fname1, dtype = dtype1, usecols=(0,1,2,3,4,5,7,8,10))

a_shock_lat = []
a_shock_lon = []
a_shock_2_lat = []
a_shock_2_lon = []

print(data)
for i in range(0, len(data)):
    if (data['Year'][i] == 1992 and (data['Month'][i] == 6  or data['Month'][i] == 7)):
        a_shock_lat.append(data['Latitude'][i])
        a_shock_lon.append(data['Longitude'][i])
    if (data['Year'][i] == 1997):
        a_shock_2_lat.append(data['Latitude'][i])
        a_shock_2_lon.append(data['Longitude'][i])
        
end = time.time()

largeEQs = np.array([[-116.267, 34.600],
            [-116.827, 34.200],
            [-116.433, 34.217]])

print('Loaded {} Total Eearthquakes', len(data))
print('Found {} Earthquakes in June – July 1992', len(a_shock_lat))
print('Found {} Earthquakes in October 1999', len(a_shock_2_lat))
print('Elapsed time is {} seconds', end - start)


plt.figure(1)
plt.axis('equal')
plt.scatter(data['Longitude'],data['Latitude'], color = 'red')
plt.scatter(a_shock_lon, a_shock_lat, color = 'blue')
plt.scatter(a_shock_2_lon, a_shock_2_lat, s = 20, color = 'green', edgecolors='black')
plt.ylim([30.0, 37.6])
plt.xlim([-122.5, -113.0])
plt.scatter(largeEQs[:,0], largeEQs[:,1], s = 50, color = 'yellow', edgecolors = 'black', marker = 'p')
plt.show()

plt.figure(2)
plt.axis('equal')
plt.scatter(data['Longitude'],data['Latitude'], color = 'red')
plt.scatter(a_shock_lon, a_shock_lat, color = 'blue')
plt.scatter(a_shock_2_lon, a_shock_2_lat, s = 20, color = 'green', edgecolors='black')
plt.ylim([33.75, 35.0])
plt.xlim([-117.1, -115.9])
plt.scatter(largeEQs[:,0], largeEQs[:,1], s = 50, color = 'yellow', edgecolors = 'black', marker = 'p')
plt.show()