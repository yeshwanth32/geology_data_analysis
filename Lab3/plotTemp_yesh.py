#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab3
"""
This code computes the sin function, y = A*np.sin(2*np.pi*x/lambda),
given an amplitude and a wavelength

Yesh 2/19/20
"""
import numpy as np
import matplotlib.pylab as plt

A = 2
pi = np.pi
y = 4
l = 24
start = 0
end = 3*l
numberOfDataPoints = 50000
i = (end- start)/numberOfDataPoints
x = np.arange(0, (3*l), i)
y = A*np.sin((2*pi*x)/l)

plt.figure()
plt.plot(x, y , lineWidth = 1.0, color="red")
plt.xlabel('Time (hours)')
plt.ylabel('Temperature Change (C)')
plt.xlim(0, 3*l)
plt.ylim(-1.25*A, 1.25*A)
plt.show()