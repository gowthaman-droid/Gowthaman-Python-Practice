limit =
expenses = []

n = int(input("How many expenses? "))

for i in range(n):
    print("\nExpense", i + 1)

    name = input("Enter expense: ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

print("\n===== EXPENSE SUMMARY =====")

total = 0
highest = expenses[0]

for expense in expenses:
    print(
        expense["name"],
        " | ",
        expense["category"],
        " | ₹",
        expense["amount"]
    )

    total = total + expense["amount"]

    if expense["amount"] > highest["amount"]:
        highest = expense

print("\nTotal spent: ₹", total)

print(
    "Highest expense:",
    highest["name"],
    "- ₹",
    highest["amount"]
)