hours = input('Number of hours worked? ')
hours = float(hours)
rate = input('What is the Pay Rate? ')
rate = float(rate)
if hours > 40 :
    standardhours = float(40)
    extrahours = hours - 40
    extrahours = float(extrahours)
    extrarate = rate * 1.5
    extrarate = float(extrarate)
    pay = (standardhours * rate) + (extrahours * extrarate)
else:
    pay = rate * hours
print(pay)