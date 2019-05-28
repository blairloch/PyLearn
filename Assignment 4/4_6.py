
def computepay(hours, rate):
    if hours > 40 :
        standardhours = float(40)
        extrahours = hours - 40
        extrahours = float(extrahours)
        extrarate = rate * 1.5
        extrarate = float(extrarate)
        pay = (standardhours * rate) + (extrahours * extrarate)
    else:
        pay = rate * hours
    return pay
    

caphours = input('Number of hours worked? ')
caphours = float(caphours)
caprate = input('What is the Pay Rate? ')
caprate = float(caprate)

print(computepay(caphours, caprate))