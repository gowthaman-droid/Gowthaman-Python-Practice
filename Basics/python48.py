
import math

u = float(input("Enter initial velocity (m/s): "))
angle = float(input("Enter launch angle (degrees): "))

theta = math.radians(angle)
g = 9.81

range_value = (u ** 2 * math.sin(2 * theta)) / g

print("Projectile Range =", round(range_value, 2), "metres")
