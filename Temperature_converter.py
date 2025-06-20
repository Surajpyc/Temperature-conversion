#entering all temperature formulas

def celtofar(c):
    return (c*(9/5)+32)
def fartocel(f):
    return ((f-32)*(5/9))
def celtokel(c):
    return c+273.15
def keltocel(k):
    return k-273.15
def fartokel(f):
    return (f - 32) * 5/9 + 273.15
def keltofar(k):
    return (k - 273.15) * 9/5 + 32

#using main fucntion to run code in loop 
def main():
    print("Temperature menu\n1. Celsius to farenheit\n2. Farenheit to celsius\n3. Celsius to kelvin\n4. Kelvin to celsius\n5. Fahrenheit to kelvin\n6. Kelvin to fahrenheit")
    n=int(input("select from the above menu:"))
    if n==1:
        c=float(input("enter temperature in celsius:"))
        print(f"{c}°C= {celtofar(c):.2f} °F")
    elif n==2:
        f=float(input("Enter temperature in farenheit:"))
        print(f"{f}°F={fartocel(f):.2f}°C")
    elif n==3:
        c=float(input("Enter temperature in celsius:"))
        print(f"{c}°C={celtokel(c):.2f}°K")
    elif n==4:
        k=float(input("Enter temperature in Kelvin:"))
        print(f"{k}={keltocel(k):.2f}°C")
    elif n==5:
        f=float(input("Enter temperature in Fahrenheit:"))
        print(f"{f}={fartokel(f):.2f}°K")
    elif n==6:
        k=float(input("Enter temperature in Kelvin:"))
        print(f"{k}={keltofar(k):.2f}°F")
    else:
        print("Invalid input")
    repeat=input("Do you want to do again [yes/no]?").lower()
    if repeat=="yes":
        main()
    else:
        exit("You chose not to do again\n\nThank you for using our application\ncome again")
main()
