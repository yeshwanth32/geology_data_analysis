#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

##
## Read in the data
##
# Use this with auxillary data
resid1, drift1, corr1, tidal1, nontide1, data1, aux1 = np.loadtxt('MFS1.out', usecols=(1,2,3,4,5,6,7), unpack=True)
# Use this with out auxillary data
#resid1, drift1, corr1, tidal1, nontide1, data1 = np.loadtxt('MFS1.out', usecols=(1,2,3,4,5,6), unpack=True)
resid2, drift2, corr2, tidal2, nontide2, data2, aux2 = np.loadtxt('MFS2.out', usecols=(1,2,3,4,5,6,7), unpack=True)

tempr=np.where (resid1 < 15)
resid_mean=resid1[tempr].mean()
i=0
for i in np.arange(len(resid1)):
    if resid1[i] > 15:
        resid1[i] = resid_mean

tempr=np.where (resid2 < 15)
resid_mean=resid2[tempr].mean()
i=0
for i in np.arange(len(resid1)):
    if resid2[i] > 15:
        resid2[i] = resid_mean

tempc=np.where (corr1 < 15)
corr_mean=corr1[tempc].mean()
i=0
for i in np.arange(len(corr1)):
    if corr1[i] > 15:
        corr1[i] = corr_mean

tempc=np.where (corr2 < 15)
corr_mean=corr2[tempc].mean()
i=0
for i in np.arange(len(corr2)):
    if corr2[i] > 15:
        corr2[i] = corr_mean

dt=10./60.
time=dt*np.arange(len(data1))/24

plt.ion()

#plt.figure(3)
plt.figure(3, figsize=[11.0,8.5])
plt.subplot(2,2,1)
plt.grid(True)
plt.gca().invert_yaxis()
#plt.plot(time, nontide1,'r-', lw=1.0, label='MFS1: Non-tidal')
#plt.plot(time, nontide2+(nontide1.max()-nontide2.max()),'b--', lw=1.0, label='MFS2: Non-tidal shifted')
#plt.plot(time, nontide2+(nontide1[0]-nontide2[0]),'b--', lw=1.0, label='MFS2: Non-tidal shifted')
plt.plot(time, data1,'r-', lw=0.5, label='MFS1: Data')
plt.plot(time, data2+(data1[0]-data2[0]),'b--', lw=0.5, label='MFS2: Data + shift')
plt.plot(time, drift1,'r-', label='MFS1: Drift')
plt.plot(time, drift2+(nontide1[0]-nontide2[0]),'b--', label='MFS2: Drift + shift')
#plt.plot(time, nontide2+(nontide1.mean()-nontide2.mean()),'b--', lw=1.0, label='MFS2: Non-tidal shifted')
#plt.plot(time, nontide2,'b--', lw=1.0, label='MFS2: Non-tidal')
#plt.plot(time, data1,'b--', lw=1.0, label='MFS1: Data', alpha=0.75)
plt.ylabel('Water Depth (m)')
plt.title('MF Well Data')
#plt.legend(loc='center left')
plt.legend(loc='upper left')
plt.subplot(2,2,2)
plt.grid(True)
#plt.plot(time, data1,'r-', label='MFS1: Data')
#plt.plot(time, drift1,'r-', label='MFS1: Drift')
#plt.plot(time, drift2,'b--', label='MFS2: Drift')
#plt.plot(time, aux1,'r-', label='MFS1: Auxillary')
plt.plot(time, corr1,'r-', label='MFS1: Correlation')
plt.plot(time, corr2,'b--', label='MFS2: Correlation')
plt.title('MFS Well Data')
plt.legend(loc='best')
plt.subplot(2,2,3)
plt.grid(True)
#plt.ylim(-0.005,0.005)
#plt.plot(time, resid1,'r-', label='MFS1: Residual')
#plt.plot(time, resid2,'b-', alpha=0.2, label='MFS2: Residual')
plt.plot(time, tidal1,'r-', label='MFS1: Tidal')
plt.plot(time, tidal2,'b-', alpha=0.2, label='MFS2: Tidal')
plt.xlabel('Days')
plt.ylabel('Amplitude (m)')
plt.legend(loc='lower left')
plt.subplot(2,2,4)
plt.grid(True)
plt.plot(time, 1*aux2,'b--', alpha=1.0, label='MFS: Barometric pressure')
#plt.plot(time, -1*aux1,'r-', label='MFS1: Barometric')
plt.xlabel('Days')
plt.legend(loc='best')

plt.savefig('MFSboth_anal.pdf')

plt.show()
