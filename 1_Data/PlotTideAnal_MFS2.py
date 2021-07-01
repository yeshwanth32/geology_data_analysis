#! /usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##
## Read in the data
##
ampO2, phaseO2 = np.loadtxt('MFS2_phases.O1', usecols=[1,2], unpack=True)

ampM2, phaseM2 = np.loadtxt('MFS2_phases.M2', usecols=[1,2], unpack=True)

window=np.arange(1,len(ampO2)+1)

plt.ion()

plt.figure(1)
plt.subplot(2,1,1)
plt.grid(True)
#plt.gca().invert_yaxis()
#plt.xlim(-50,450)
#plt.ylim(4,0)
plt.plot(window, ampO2, 'b*-', label='MFS2 O1')
plt.plot(window, ampM2, 'b*--', label='MFS2 M2')
plt.ylabel('Amplitude')
plt.title('MFS Tidal analysis -- Well MFS2')
#plt.legend(loc='upper left')
plt.legend(loc='best')
plt.subplot(2,1,2)
plt.grid(True)
#plt.gca().invert_yaxis()
#plt.xlim(-50,450)
#plt.ylim(4,0)
plt.plot(window, phaseO2, 'b*-', label='MFS2 O1')
plt.plot(window, phaseM2, 'b*--', label='MFS2 M2')
plt.xlabel('Window')
plt.ylabel('Phase')
plt.legend(loc='best')

plt.savefig('MFS2_Phases.pdf')

plt.show()
