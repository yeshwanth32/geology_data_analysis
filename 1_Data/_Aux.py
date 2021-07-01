#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

##
## Read in the data
##
# Use this line when using the auxillary data
resid1, drift1, corr1, tidal1, nontide1, data1, aux1 = np.loadtxt('MFS1.out', usecols=(1,2,3,4,5,6,7), unpack=True)
# Use this line when not using the auxillary data
#resid1, drift1, corr1, tidal1, nontide1, data1 = np.loadtxt('MFS1.out', usecols=(1,2,3,4,5,6), unpack=True)
resid2, drift2, corr2, tidal2, nontide2, data2, aux2 = np.loadtxt('MFS2.out', usecols=(1,2,3,4,5,6,7), unpack=True)

tempr=np.where (resid1 < 15)
resid_mean=resid1[tempr].mean()
i=0
for i in np.arange(len(resid1)):
    if resid1[i] > 15:
        resid1[i] = resid_mean

tempc=np.where (corr1 < 15)
corr_mean=corr1[tempc].mean()
i=0
for i in np.arange(len(corr1)):
    if corr1[i] > 15:
        corr1[i] = corr_mean

dt=10.0/60.0
time=dt*np.arange(len(data1))/24

plt.ion()

#plt.figure(1)
plt.figure(3, figsize=[12,8])
plt.subplot(3,1,1)
plt.grid(True)
#plt.gca().invert_yaxis()
#plt.xlim(-50,450)
#plt.ylim(4,0)
plt.plot(time, aux1,'r-', lw=1.0, label='MFS1: Tidal')
plt.ylabel('Water Depth (m)')
plt.title('MFS Well Data')
plt.legend(loc='lower right')
plt.subplot(3,1,2)
plt.grid(True)
#plt.xlim(-50,450)
#plt.ylim(0,18)
#plt.gca().invert_yaxis()
plt.plot(time, aux2,'b-', lw=1.0, label='MFS2: Tidal')
plt.ylabel('Amplitude (m)')
plt.legend(loc='lower right')
plt.subplot(3,1,3)
plt.grid(True)
#plt.xlim(-50,450)
#plt.ylim(0,18)
plt.plot(time, aux1/aux1.max(),'r-', label='MFS1: Tidal')
plt.plot(time, aux2/aux2.max(),'b-', label='MFS2: Tidal')
plt.xlabel('Days')
plt.ylabel('Amplitude (m)')
plt.legend(loc='lower right')
plt.xlabel('Days')
plt.legend(loc='lower left')

plt.savefig('MFSboth_anal.pdf')

plt.show()
