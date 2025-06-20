
# Temperature Conversion Calculations

This Python script performs various temperature conversions among Celsius, Fahrenheit, and Kelvin using individual functions.

## Conversions Covered

- Kelvin to Celsius
- Celsius to Fahrenheit
- Fahrenheit to Kelvin
- Celsius to Kelvin
- Fahrenheit to Celsius
- Kelvin to Fahrenheit

## How it Works

### Kelvin to Celsius
```python
def keltocel(k):
    return k - 273.15
```

### Celsius to Fahrenheit
```python
def celtofah(c):   
    return ((9/5) * c) + 32
```

### Fahrenheit to Kelvin
```python
def fahtokel(f):
    return ((f - 32) * (5/9)) + 273.15
```

### Celsius to Kelvin
```python
kelvin = 273.15 + c
```

### Fahrenheit to Celsius
```python
celsius = ((5/9) * (f - 32))
```

### Kelvin to Fahrenheit
```python
fahrenheit = ((k - 273.15) * (9/5)) + 32
```

## Example Output

The script takes input in Kelvin, converts it to Celsius, then to Fahrenheit, Kelvin, and back in different orders to demonstrate all conversions.

## Author

- Created by Suraj Gupta

## License

Open-source, free to use.
