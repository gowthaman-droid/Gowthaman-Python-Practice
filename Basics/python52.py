
import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation")
else:
    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("Two distinct roots:", x1, x2)

    elif D == 0:
        x = -b / (2*a)
        print("Two equal roots:", x)

    else:
        real = -b / (2*a)
        imaginary = math.sqrt(-D) / abs(2*a)
        print("Complex roots:")
        print(real, "+", imaginary, "i")
        print(real, "-", imaginary, "i")
