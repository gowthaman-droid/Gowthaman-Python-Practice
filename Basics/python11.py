import calendar
day=int(input("Enter your brith date: "))
month=int(input("Enter your brith month: "))
year=int(input("Enter your brith year: "))
print(calendar.month(year,month))
print(f"Your Birthday is: {day}/{month}/{year}")
