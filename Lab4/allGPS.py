#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab4
"""
This code extracts GPS data from two locations in iceland and creates three
subplots showing the north, east and vertical positions of the GPS data.

Yesh 2/26/2020
"""
import numpy as np
import matplotlib.pylab as plt
import urllib.request

loc1 = 'FLRS'
loc2 = 'PDEL'

temp_f1 = "http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/" +loc1+ ".tenv3"
temp_f2 = "http://geodesy.unr.edu/gps_timeseries/tenv3/IGS14/" +loc2+ ".tenv3"

fname1 = loc1 + '.IGS08.tenv3'
fname2 = loc2 + '.IGS08.tenv3'

urllib.request.urlretrieve(temp_f1, fname1)
urllib.request.urlretrieve(temp_f2, fname2)

dtype1 = np.dtype([('East position', 'f8')
, ('North position', 'f8'), ('Vertical position', 'f8')])


data_1 = np.loadtxt(fname1, dtype=dtype1, skiprows=1, usecols=(8,10,12))
data_2 = np.loadtxt(fname2, dtype=dtype1, skiprows=1, usecols=(8,10,12))



def getGPSstats(data):
    numberOfDays = len(data['East position'])
    totalTime = numberOfDays/365
    totalEastDisplacement = (data['East position'][-1] - data['East position'][0])*100
    totalNorthDisplacement = (data['North position'][-1] - data['North position'][0])*100
    totalVerticalDisplacement = (data['Vertical position'][-1] - data['Vertical position'][0])*100
    averageEastVelocity = totalEastDisplacement/totalTime
    averageNorthVelocity = totalNorthDisplacement/totalTime
    averageVerticalVelocity = totalVerticalDisplacement/totalTime
    
    print('Time Span: ','{:.4}'.format(totalTime),'years')
    print('Number of days with data: ',numberOfDays,'years')
    print('Total north displacement: ','{:.4}'.format(totalNorthDisplacement),'cm')
    print('Total east displacement: ','{:.4}'.format(totalEastDisplacement),'cm')
    print('Total vertica displacement: ','{:.4}'.format(totalVerticalDisplacement),'cm')
    print('Average north displacement: ','{:.2}'.format(averageNorthVelocity),'cm/year')
    print('Average east displacement: ','{:.2}'.format(averageEastVelocity),'cm/year')
    print('Average vertical displacement: ','{:.2}'.format(averageVerticalVelocity),'cm/year')
    print('')


getGPSstats(data_1)
getGPSstats(data_2)


dates1 = np.arange(0,len(data_1['East position']))
dates2 = np.arange(0,len(data_2['East position']))

fig = plt.figure(figsize=(10,10))

plt.figure(1)
plt.subplot(3, 1, 1)
plt.plot(dates1,data_1['North position'], color = 'red', label = loc1)
plt.plot(dates2,data_2['North position'], color = 'blue', label = loc2)
plt.grid(True)
plt.xlabel('Number of days since recording data')
plt.ylabel('North Position')
plt.legend(loc="upper left")

plt.subplot(3, 1, 2)
plt.plot(dates1,data_1['East position'], color = 'red', label = loc1)
plt.plot(dates2,data_2['East position'], color = 'blue', label = loc2)
plt.grid(True)
plt.xlabel('Number of days since recording data')
plt.ylabel('East Position')
plt.legend(loc="upper left")

plt.subplot(3, 1, 3)
plt.plot(dates1,data_1['Vertical position'], color = 'red', label = loc1)
plt.plot(dates2,data_2['Vertical position'], color = 'blue', label = loc2)
plt.grid(True)
plt.xlabel('Number of days since recording data')
plt.ylabel('Vertical Position')
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()


