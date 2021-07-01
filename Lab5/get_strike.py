#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab5
"""
This code calculates strike given dip direction

Yesh 3/2/2020
"""
import sys


try:
    dipDirection = float(input('give me dip !!'))
except ValueError:
    print('Error')
    print('DipDirection must be an float between 0 and 360')
    sys.exit()
if (dipDirection < 0 or dipDirection > 360):
    print('Error!')
    print('DipDirection must be between 0 and 360')
    sys.exit()
    
strike = dipDirection - 90
if (strike < 0):
    strike = 360 - abs(strike)
print("Dip Direction ", '{:03d}'.format(round(dipDirection)))
print("Strike", '{:03d}'.format(round(strike)))

