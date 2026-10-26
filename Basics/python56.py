
import math

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    value = float(input("Enter a number: "))
    numbers.append(value)

mean = sum(numbers) / n

variance = sum((x - mean) ** 2 for x in numbers) / n

std_dev = math.sqrt(variance)

print("Mean =", round(mean, 2))
print("Variance =", round(variance, 2))
print("Standard Deviation =", round(std_dev, 2))
