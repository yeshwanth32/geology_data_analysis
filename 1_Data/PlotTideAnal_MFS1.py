#! /usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##
## Read in the data
##
ampO1, phaseO1 = np.loadtxt('MFS1_phases.O1', usecols=[1,2], unpack=True)
#ampO2, phaseO2 = np.loadtxt('MFS2_phases.O1', usecols=[1,2], unpack=True)

ampM1, phaseM1 = np.loadtxt('MFS1_phases.M2', usecols=[1,2], unpack=True)
#ampM2, phaseM2 = np.loadtxt('MFS2_phases.M2', usecols=[1,2], unpack=True)

#dt=10.0/60.0
#time=dt*np.arange(len(ampO1))/24
window=np.arange(1,len(ampO1)+1)

plt.ion()

plt.figure(3)
plt.subplot(2,1,1)
plt.grid(True)
#plt.gca().invert_yaxis()
#plt.xlim(-50,450)
#plt.ylim(4,0)
plt.plot(window, ampO1, 'ro-', label='MFS1 O1')
plt.plot(window, ampM1, 'ro--', label='MFS1 M2')
plt.ylabel('Amplitude')
plt.title('MFS Tidal analysis -- Well MFS1')
#plt.legend(loc='upper left')
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.grid(True)
#plt.gca().invert_yaxis()
#plt.xlim(-50,450)
#plt.ylim(4,0)
plt.plot(window, phaseO1, 'ro-', label='MFS1 O1')
plt.plot(window, phaseM1, 'ro--', label='MFS1 M2')
plt.xlabel('Window')
plt.ylabel('Phase')
plt.legend(loc='best')

plt.savefig('MFS1_Phases.pdf')

plt.show()
