
# Temperature Conversion Application

This is a simple Python program that allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin using a menu-driven approach.

## Features

- Celsius to Fahrenheit
- Fahrenheit to Celsius
- Celsius to Kelvin
- Kelvin to Celsius
- Fahrenheit to Kelvin
- Kelvin to Fahrenheit

## How to Use

1. Run the script.
2. Select a conversion option from the menu (1 to 6).
3. Enter the temperature value when prompted.
4. View the converted result.
5. Choose whether to perform another conversion.

## Code Example

```python
def celtofar(c):
    return (c * (9 / 5) + 32)
def fartocel(f):
    return ((f - 32) * (5 / 9))
def celtokel(c):
    return c + 273.15
def keltocel(k):
    return k - 273.15
def fartokel(f):
    return (f - 32) * 5 / 9 + 273.15
def keltofar(k):
    return (k - 273.15) * 9 / 5 + 32

def main():
    print("Temperature menu\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n3. Celsius to Kelvin\n4. Kelvin to Celsius\n5. Fahrenheit to Kelvin\n6. Kelvin to Fahrenheit")
    n = int(input("Select from the above menu: "))
    if n == 1:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celtofar(c):.2f} °F")
    elif n == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fartocel(f):.2f}°C")
    elif n == 3:
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C = {celtokel(c):.2f}K")
    elif n == 4:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {keltocel(k):.2f}°C")
    elif n == 5:
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F = {fartokel(f):.2f}K")
    elif n == 6:
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K = {keltofar(k):.2f}°F")
    else:
        print("Invalid input")
    repeat = input("Do you want to do again [yes/no]? ").lower()
    if repeat == "yes":
        main()
    else:
        exit("You chose not to do again\n\nThank you for using our application\nCome again")

main()
```

## Author

- Created by Suraj Gupta

## License

This project is open-source and free to use.
