#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab4
"""
This code computes the volumes of different layers of earth and creates 
a pie chart out of it

Yesh 2/26/2020
"""

import numpy as np
import matplotlib.pylab as plt

def volSphere(radius):
    return (4/3)*np.pi*np.power(radius,2)


#thicknesses of Earth’s layers in km
core=3486
mantle=2850
crust=35

VolTotal = volSphere(core+mantle+crust)
VolCore = volSphere(core)
VolMantle = volSphere(mantle+core) - VolCore
VolCrust = volSphere(crust+mantle+core) - (VolMantle + VolCore)
pctVolCore = (VolCore/VolTotal)
pctVolMantle = (VolMantle/VolTotal)
pctVolCrust = (VolCrust/VolTotal)

print("Volume of core\t",'{:.2E}'.format(VolCore), "Km^3")
print("Volume of mantle",'{:.2E}'.format(VolMantle),"km^3")
print("Volume of crust\t" , '{:.2E}'.format(VolCrust), "km^3")
print("Core:\t", '{:.1%}'.format(pctVolCore), "%")
print("Mantle:\t", '{:.1%}'.format(pctVolMantle), "%")
print("Crust:\t", '{:.1%}'.format(pctVolCrust), "%")

explode = [0.1,0.1,0.1]
labels = ['Core ' + '{:.1%}'.format(pctVolCore),'Mantle ' + '{:.1%}'.format(pctVolMantle)
         ,'Crust ' + '{:.1%}'.format(pctVolCrust)]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
plt.figure(1)
plt.set_cmap('summer') # Have to figure out the colormaps
plt.pie([pctVolCore,pctVolMantle,pctVolCrust], explode = explode, labels = labels, colors = colors)
plt.show()

