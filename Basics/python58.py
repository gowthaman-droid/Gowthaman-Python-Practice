
import math

T0 = float(input("Enter initial temperature (°C): "))
Ts = float(input("Enter surrounding temperature (°C): "))
k = float(input("Enter cooling constant: "))
t = float(input("Enter time elapsed: "))

if k < 0 or t < 0:
    print("Cooling constant and time must be non-negative.")
else:
    T = Ts + (T0 - Ts) * math.exp(-k * t)

    print("Temperature after time =", round(T, 2), "°C")
