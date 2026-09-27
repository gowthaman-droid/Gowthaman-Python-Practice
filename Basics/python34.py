import numpy as np

marks = np.array(list(map(int, input("Enter 5 marks: ").split())))

print("Total =", np.sum(marks))
print("Average =", np.mean(marks))
print("Highest =", np.max(marks))
print("Lowest =", np.min(marks))