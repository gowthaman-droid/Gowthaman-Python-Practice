limit = float(input("Enter monthly data limit (GB): "))

total_used = 0

days = int(input("Enter number of days: "))

for i in range(1, days + 1):
    usage = float(input(f"Enter data used on Day {i} (GB): "))
    total_used += usage

remaining = limit - total_used
percentage = (total_used / limit) * 100

print("\n--- Data Usage Report ---")
print("Total Used:", total_used, "GB")
print("Remaining:", max(remaining, 0), "GB")
print("Usage:", round(percentage, 2), "%")

if percentage >= 100:
    print("Status: DATA LIMIT EXCEEDED!")
elif percentage > 90:
    print("Status: Critical")
elif percentage >= 75:
    print("Status: Warning")
else:
    print("Status: Normal")