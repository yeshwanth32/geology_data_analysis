#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

##
## Read in the data
##
resid, drift, corr, tidal, nontide, data, aux = np.loadtxt('MFS2.out', usecols=(1,2,3,4,5,6,7), unpack=True)

tempr=np.where (resid < 15)
resid_mean=resid[tempr].mean()
i=0
for i in np.arange(len(resid)):
    if resid[i] > 15:
        resid[i] = resid_mean

tempc=np.where (corr < 15)
corr_mean=corr[tempc].mean()
i=0
for i in np.arange(len(corr)):
    if corr[i] > 15:
        corr[i] = corr_mean

dt=10./60.0
time=dt*np.arange(len(data))/24

plt.ion()

#plt.figure(2)
plt.figure(2, figsize=[12,8])
plt.subplot(2,2,1)
plt.grid(True)
plt.gca().invert_yaxis()
#plt.xlim(-50,450)
#plt.ylim(4,0)
plt.plot(time, nontide,'r-', lw=1.0, label='Non-tidal')
#plt.plot(time, data,'b-', lw=1.0, label='Data', alpha=0.75)
plt.plot(time, drift,'m-', lw=1.0, label='Drift', alpha=0.75)
plt.ylabel('Water Depth (m)')
plt.title('MFS-2 Well Data')
plt.legend(loc='upper left')
plt.subplot(2,2,2)
plt.grid(True)
#plt.xlim(-50,450)
#plt.ylim(0,18)
plt.gca().invert_yaxis()
#plt.plot(time, data,'b-', label='Data')
#plt.plot(time, drift,'y-', label='Drift')
#plt.plot(time, aux,'y-', label='Auxillary')
plt.plot(time, corr,'c-', label='Correlation')
plt.title('MFS-2 Well Data')
plt.legend(loc='upper right')
plt.subplot(2,2,3)
plt.grid(True)
#plt.xlim(-50,450)
#plt.ylim(0,18)
plt.plot(time, resid,'r-', label='Residual')
plt.xlabel('Days')
plt.ylabel('Amplitude (m)')
plt.legend(loc='lower left')
plt.subplot(2,2,4)
plt.grid(True)
#plt.xlim(-50,450)
#plt.ylim(0,18)
#plt.plot(time, resid,'r-', label='Residual')
plt.plot(time, tidal,'b-', label='Tidal')
plt.xlabel('Days')
plt.legend(loc='lower left')

plt.savefig('MFS2_anal.pdf')

plt.show()
