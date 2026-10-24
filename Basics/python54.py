
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Sides must be positive.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle.")
else:
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("Semi-perimeter =", s)
    print("Area =", round(area, 2))
