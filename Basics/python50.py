
p = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan duration (years): "))

r = annual_rate / (12 * 100)
n = years * 12

if r == 0:
    emi = p / n
else:
    emi = p * r * (1 + r) ** n / ((1 + r) ** n - 1)

total_payment = emi * n
total_interest = total_payment - p

print("Monthly EMI =", round(emi, 2))
print("Total Payment =", round(total_payment, 2))
print("Total Interest =", round(total_interest, 2))
