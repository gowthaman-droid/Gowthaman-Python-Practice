w = float(input("Enter weight in kg: "))
h = float(input("Enter height in metres: "))

bmi = w / (h ** 2)

print("BMI =", round(bmi, 2))