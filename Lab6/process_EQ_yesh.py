#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab6
"""
This code extracts GPS data from an Earth Quake in calfornia and plots the locations

Yesh 2/26/2020
"""

import numpy as np 

import datetime as dt
import time
import matplotlib.pylab as plt

northridge_lon = [-118.535]
northridge_lat = [34.207]

dtype1 = np.dtype([('Year', 'i4'),('Month', 'i4'),('Day', 'i4'),('Hour', 'i4')
                   ,('Minute', 'i4'),('Seconds', 'f8'), ('Latitude', 'f8')
                   ,('Longitude', 'f8'),('Magnitude', 'f8'),])

fname1 = 'C:\\Users\\yeshw\\Desktop\\Umass\\Geology_497\\Lab6\\NorthridgeEQ.dat';

start = time.time()

data = np.loadtxt(fname1, dtype = dtype1, usecols=(0,1,2,3,4,5,7,8,10))

EQdate = dt.datetime(1994, 1, 1)

a_shock_lon = []
a_shock_lat = []
f_shock_lon = []
f_shock_lat = []
pltdata_1_lat = []
pltdata_1_lon = []
pltdata_2_lat = []
pltdata_2_lon = []

for i in range(0, len(data) - 10000):
    year = data['Year'][i]
    month = data['Month'][i]
    day = data['Day'][i]
    hour = data['Hour'][i]
    lat = data['Latitude'][i]
    lon = data['Longitude'][i]
    date = dt.datetime(year, month, day, hour)
    if ((lat >= 30.0 and lat <= 37.6) and (lon >= -122.5 and lon <= -113.0)):
        pltdata_1_lat.append(data['Latitude'][i])
        pltdata_1_lon.append(data['Longitude'][i])
        
    if ((lat >= 33.8 and lat <= 34.8) and (lon >= -119.0 and lon <= -118.0)):       
        if ((date - EQdate).days < 100 and (date - EQdate).days > 0):      
            a_shock_lon.append(lon)
            a_shock_lat.append(lat)
        if ((date - EQdate).days > -100 and (date - EQdate).days < 0):             
            f_shock_lon.append(lon)
            f_shock_lat.append(lat)
        pltdata_2_lat.append(data['Latitude'][i])
        pltdata_2_lon.append(data['Longitude'][i])
            
end = time.time()

print("Loaded \t", len(data), " Earthquakes" )
print("Found \t", len(a_shock_lon), "\t aftershocks" )
print("Found \t", len(f_shock_lon), "\t potential foreshocks" )
print("Elapsed time is ", '{:.3f}'.format(end - start), "seconds" )


plt.figure(1, figsize=(10,10))
plt.axis('equal')
plt.scatter(pltdata_1_lat, pltdata_1_lon, color = 'red')
plt.scatter(a_shock_lat, a_shock_lon, color = 'blue')
plt.scatter(f_shock_lat, f_shock_lon, s = 20, color = 'green', edgecolors='black')
plt.scatter(northridge_lat, northridge_lon, s = 24, color = 'yellow', edgecolors = 'black', marker = 'p')
plt.show()

plt.figure(2, figsize=(10,10))
plt.axis('equal')
plt.scatter(pltdata_2_lat, pltdata_2_lon, color = 'red')
plt.scatter(a_shock_lat, a_shock_lon, color = 'blue')
plt.scatter(f_shock_lat, f_shock_lon, s = 20, color = 'green', edgecolors='black')
plt.scatter(northridge_lat, northridge_lon, s = 30, color = 'yellow', edgecolors = 'black', marker = 'p')
plt.show()

#print(data_dates) 