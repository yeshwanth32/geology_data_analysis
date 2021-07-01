# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:30:13 2020

program sinwave2.py
computes a sin wave using arrays

@author: yeshw
"""

import numpy as np

sinewave = np.zeros(91,float)

for i in np.arange(0,91):
    theta = i * np.pi / 180.0
    sinewave[i] = np.sin(theta)
    """print ('sin', i, 'is' , np.sin(theta))"""

print (sinewave)
print (np.arange(0,91).size)