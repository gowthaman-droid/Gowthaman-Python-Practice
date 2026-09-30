import numpy as np

celsius = np.array(list(map(float, input("Enter temperatures in Celsius: ").split())))

fahrenheit = (celsius * 9/5) + 32

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)