p=1000
g=9.81
h=float(input("Enter the height difference: "))
print(f"Formula\nΔP = ρgh\nDensity of Water ρ=1000\nacceleration due to gravity = 9.81 m/s\nHeight difference of liquid = {h}m")
print(f"Calculation: ΔP = 1000 x 9.81 x {h}")
a=p*g*h
print(f"ΔP = {a}")
