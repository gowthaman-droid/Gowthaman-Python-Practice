
speed_kmh = float(input("Enter vehicle speed (km/h): "))
deceleration = float(input("Enter braking deceleration (m/s^2): "))

speed = speed_kmh * 5 / 18

distance = speed ** 2 / (2 * deceleration)

print("Braking Distance =", round(distance, 2), "metres")
