import numpy as np
units=np.array(input("Enter the units spent: ").split(), dtype=float)
total_units=units.sum()
max=units.max()
mean=units.mean()
min=units.min()

print(f"Total units spent: {total_units}")
print(f"Maximum units spent: {max}")        
print(f"Mean units spent: {mean}")
print(f"Minimum units spent: {min}")
