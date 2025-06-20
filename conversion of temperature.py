#kelvin to celsius

k=float(input("Enter value in kelvin:"))
def keltocel(k):
    return k-273.15
c=keltocel(k)
print(f"{c:.2f}° C")

#celsius to fahrenheit

def celtofah(c):   
    return ((9/5) * c)+32
f=celtofah(c)
print(f"{f:.2f}°F")

#farenheit to kelvin

def fahtokel(f):
    return (((f-32) * (5/9)) + 273.15)
kl=fahtokel(f)
print(f"{kl:2f}°K")

#celsius to kelvin
kelvin=273.15 + c
print(f"{kelvin:.2f}°K")

#fahrenheit to celsius
celsius=(((5/9)*(f -32)))
print(f"{celsius:.2f}°C")

#kelvin to fahrenheit
fahrenheit=(((k-273.15)*(9/5))+32)
print(f"{fahrenheit:.2f}°F")
