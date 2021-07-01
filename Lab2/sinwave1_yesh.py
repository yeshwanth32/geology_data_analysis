# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 20:30:13 2020

program sinwave1.py
computes a sin wave

@author: yeshw
"""

import numpy as np

for i in np.arange(0,91):
    theta = i * np.pi/180
    print ('sin', i, 'is' , np.sin(theta), sep = ' ', end = '\n\b')
    