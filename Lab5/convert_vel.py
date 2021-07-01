#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab4
"""
This code converts velocities

Yesh 3/2/2020
"""
inputUnits = input('Specify units (mph or m/s)')

if (inputUnits != 'mph' and inputUnits != 'm/s'):
    inputUnits = 'mph'

try:
    inputVel = float(input('Enter the velocity '))
except ValueError:
    inputVel = 10.0

if (inputUnits == 'mph'):
    try:
        convertUnit = float(input('Enter 1 to convert to m/s or Enter 2 to convert to Km/hr'))
    except ValueError:
        convertUnit = 1.0
    if (convertUnit == 1):
        print(inputVel, ' ' , inputUnits, ' = ', '{:.2f}'.format(inputVel/2.237), ' m/s')
    else:
        print(inputVel, ' ' , inputUnits, ' = ', '{:.2f}'.format(inputVel*1.609), ' km/hr')
else:
    try:
        convertUnit = float(input('Enter 1 to convert to mph or Enter 2 to convert to Km/hr'))
    except ValueError:
        convertUnit = 1.0
    if (convertUnit == 1):
        print(inputVel, ' ' , inputUnits, ' = ', '{:.2f}'.format(inputVel*2.237), ' mph')
    else:
        print(inputVel, ' ' , inputUnits, ' = ', '{:.2f}'.format(inputVel*3.6), ' km/hr')
