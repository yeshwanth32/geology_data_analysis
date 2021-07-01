#! C:\Users\yeshw\Desktop\Umass\Geology_497\Lab4
"""
This code returns rock type based on its composition

Yesh 3/2/2020
"""

exit = False
while exit == False:
    def name_that_rock(Na2O, K2O, SiO2):
        sum = Na2O + K2O
        if ((SiO2 > 45 and SiO2 < 52) and (sum > 0 and sum < 5)):
            return "Basalt"
        elif ((SiO2 > 52 and SiO2 < 63) and (sum > 0 and sum < 6)):
            return "Andesite"
        elif ((SiO2 > 69 and SiO2 < 77) and (sum > 6 and sum < 16)):
            return "Rhyolite"
        return "unknown"
    
    sampleLabel = input('Enter sample label (Enter -1 to break)')
    if (sampleLabel == '-1'):
        break
    
    try:
        Na2O = float(input('Enter the weight percent for Na2O (default is 4.26):'))
    except ValueError:
        print('Default value taken')
        Na2O = 4.26
    
    try:
        K2O = float(input('Enter the weight percent for K2O (default is 1.02):'))
    except ValueError:
        print('Default value taken')
        K2O = 1.02
        
    try:
        SiO2 = float(input('Enter the weight percent for SiO2 (default is 62.75):'))
    except ValueError:
        print('Default value taken')
        SiO2 = 62.75
    
    print('Rock ', sampleLabel, ': ', name_that_rock(Na2O, K2O, SiO2))
