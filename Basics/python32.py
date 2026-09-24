n = int(input("Number of people: "))
names = []
spent = {}

for i in range(n):
    name = input("Enter name: ")
    names.append(name)
    spent[name] = 0

for name in names:
    amt = int(input(f"{name} spent: "))
    spent[name] += amt

total = sum(spent.values())
share = total // n

print("Each should pay:", share)
for name in names:
    if spent[name] > share:
        print(name, "gets", spent[name] - share)
    elif spent[name] < share:
        print(name, "owes", share - spent[name])
    else:
        print(name, "settled")