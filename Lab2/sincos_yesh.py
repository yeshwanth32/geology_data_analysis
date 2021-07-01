# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:37:51 2020

program sincos.py
compute and plot sin and cos waves using arrays

@author: yeshw
"""

import numpy as np
import matplotlib.pylab as plt

a = 0
b = 90

sinwave = np.zeros(np.abs(b-a)+1,float)
coswave = np.zeros(np.abs(b-a)+1,float)

j = 0
for i in np.arange(a,b+1):
    theta = i * np.pi / 180.0
    sinwave[j] = np.sin(theta)
    coswave[j] = np.cos(theta)
    j = j+1

plt.figure(1)
plt.grid(True)
plt.plot(sinwave, label = 'sin')
plt.plot(coswave, label = 'cos')
plt.title('Trig function plot')
plt.xlabel('Angle (degrees)')
plt.ylabel('Function value')
plt.legend()
plt.show()