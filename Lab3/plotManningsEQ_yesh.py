#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab3
"""
This code analyzes the data in the file MinkRiver.dat. It uses mannings equation
to calculate 5 potential flow velocities using different roughness values, it then
plots the data in the minkriver data file to approximate the roughness value of the river

Yesh 2/19/20
"""

import numpy as np
import matplotlib.pylab as plt

loc1Dat= [[1.6912,1.5982],
         [0.9642,1.1151],
         [1.254,1.512],
         [1.3764,1.3266],
         [1.1394,1.3791],
         [1.703,1.7386],
         [1.1346,1.2492],
         [0.60396,0.97686],
         [1.6697,2.0005],
         [0.55459,0.72213]]
loc2Dat = np.loadtxt('Mink River.dat' ,skiprows = 2, delimiter = ',')

loc1Dat = np.array(loc1Dat)
loc2Dat = np.array(loc2Dat)

K = 1.0
roughnessValues = [0.01,0.025,0.05,0.075,0.100]
h = np.arange(0,3.01,0.01)
S = 0.001
Vs = []

for i in np.arange(0, len(roughnessValues)):
    Vs.append((K/roughnessValues[i])*(h**(2/3))*(S**(1/2)))

#print(Vs[0])
plt.figure()
plt.scatter(loc2Dat[:,1],loc2Dat[:,0], s=10, facecolors='black',
            edgecolors='black', label = 'Location 2')
plt.scatter(loc1Dat[:,1],loc1Dat[:,0], s=10, facecolors='none',
            edgecolors='r', label = 'Location 1')
plt.plot(h,Vs[0],'--',lineWidth = 1.0, color="black", label = 'V1')
plt.plot(h,Vs[1],'-.',lineWidth = 1.0, color="blue", label = 'V2')
plt.plot(h,Vs[2],':',lineWidth = 1.0, color="green", label = 'V3')
plt.plot(h,Vs[3],'-.',lineWidth = 1.0, color="red", label = 'V4')
plt.plot(h,Vs[4],',',lineWidth = 1.0, color="magenta", label = 'V5')
plt.xlabel('Stream Stage (m)')
plt.ylabel('Flow Velocity (m/s)')
plt.xlim(0, 2.5)
plt.ylim(0, 5)
plt.legend()
plt.show()

print("Location 1 roughness coefficient = ", 0.025)
print("Location 2 roughness coefficient = ", 0.05)

#plt.scatter(loc2Dat[:,1],loc2Dat[:,0])
