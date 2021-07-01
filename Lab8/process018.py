# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:49:03 2020

@author: yeshw
"""

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import numpy as np

dtypes = {'sample ID': 'str', 'depth': 'float', 'age': 'float', '180': 'str'}

try:
    benthic = pd.read_table('benthic.dat', skiprows = 8, dtype = dtypes,  engine = 'python' , sep='\*\|\*')
    planktonic = pd.read_table('planktonic.dat', skiprows = 8, dtype = dtypes, engine ='python' , sep='\*\|\*')
except IOError:
    print('error reading file')
    
df_b = pd.DataFrame(benthic)
df_p = pd.DataFrame(planktonic)

print('Found {} Total Benthic Isotope Values Found {} Total Planktonic Isotope Values'.format(len(df_b), len(df_p)))

b_180 = []
p_180 = []
b_time = []
p_time = []

for i in df_b.values:
    b_time.append(float(re.findall("\d+\.\d+", i[0])[1])*1000)
    b_180.append(float(i[0][-5:]))
for i in df_p.values:
    p_time.append(float(re.findall("\d+\.\d+", i[0])[1])*1000)
    p_180.append(float(i[0][-5:]))

plt.plot(b_time, b_180)
plt.tight_layout()
plt.vlines([1000],3.0,5.0)
plt.xlabel('Time Before Present (kyr)')
plt.ylabel('Benthic δ18O (permille)')
plt.show()

plt.plot(p_time, p_180)
plt.tight_layout()
plt.vlines([1000],-0.0,-2.5)
plt.xlabel('Time Before Present (kyr)')
plt.ylabel('Planktonic δ18O (permille)')
plt.show()



#print(df_b.iloc[:,[1,2,3]].as_matrix())