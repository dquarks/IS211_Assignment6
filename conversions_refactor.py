def convertCelsiusToKelvin(c):
    return c + 273.15

def convertKelvinToFahrenheit(k):
    return k * (9/5) - 459.67

def convertFahrenheitToCelsius(f):
    return (f - 32) * (5/9)

def convert(fromUnit, toUnit, value):
    t = 0
    if(fromUnit.lower() == toUnit.lower()):
        t = value
    elif(fromUnit.lower() == 'c' and toUnit.lower() == 'k'):
        t = convertCelsiusToKelvin(value)
    elif(fromUnit.lower() == 'k' and toUnit.lower() == 'f'):
        t = convertKelvinToFahrenheit(value)
    elif(fromUnit.lower() == 'f' and toUnit.lower() == 'c'):
        t = convertFahrenheitToCelsius(value)
    elif(fromUnit.lower() == 'k' and toUnit.lower() == 'c'):
        t = convertFahrenheitToCelsius(convertKelvinToFahrenheit(value))
    elif(fromUnit.lower() == 'c' and toUnit.lower() == 'f'):
        t = convertKelvinToFahrenheit(convertCelsiusToKelvin(value))
    elif(fromUnit.lower() == 'f' and toUnit.lower() == 'k'):
        t = convertCelsiusToKelvin(convertFahrenheitToCelsius(value))
    return ('%s -> %s: %.5f' % (fromUnit, toUnit, t))

print(convert('C', 'K', 100.00))
print(convert('K', 'F', 100.00))
print(convert('F', 'C', 100.00))
print(convert('K', 'C', 100.00))
print(convert('C', 'F', 100.00))
print(convert('F', 'K', 100.00))
print(convert('F', 'F', 100.00))
print(convert('C', 'C', 100.00))
print(convert('K', 'K', 100.00))

# C -> K -> F -> C ...
