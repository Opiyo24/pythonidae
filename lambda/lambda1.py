def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celcius(T):
    return (float(5)/9)*(T - 32)
temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celcius, F)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_celcius = list(map(celcius, temperatures_in_Fahrenheit))

print(temperatures_in_Fahrenheit)
print(temperatures_in_celcius)