items = []

def add_item():
    item_type = input("Enter type (Lost/Found): ")
    name = input("Enter item name: ")
    location = input("Enter location: ")
    owner = input("Enter your name: ")
    phone = input("Enter contact number: ")

    item = {
        "type": item_type,
        "name": name,
        "location": location,
        "owner": owner,
        "phone": phone,
        "status": "Not Returned"
    }

    items.append(item)
    print("Item added successfully!")


def search_item():
    search = input("Enter item name to search: ").lower()

    found = False

    for item in items:
        if search in item["name"].lower():
            print("\nItem Found")
            print("Type:", item["type"])
            print("Name:", item["name"])
            print("Location:", item["location"])
            print("Reported by:", item["owner"])
            print("Contact:", item["phone"])
            print("Status:", item["status"])
            found = True

    if not found:
        print("No matching item found.")


def display_items():
    if len(items) == 0:
        print("No items reported.")
        return

    for i, item in enumerate(items, 1):
        print("\nItem", i)
        print("Type:", item["type"])
        print("Name:", item["name"])
        print("Location:", item["location"])
        print("Reported by:", item["owner"])
        print("Status:", item["status"])


def return_item():
    name = input("Enter item name to mark as returned: ").lower()

    for item in items:
        if item["name"].lower() == name:
            item["status"] = "Returned"
            print("Item marked as returned.")
            return

    print("Item not found.")


while True:
    print("\n===== CAMPUS LOST & FOUND =====")
    print("1. Add Lost/Found Item")
    print("2. Search Item")
    print("3. Display All Items")
    print("4. Mark Item as Returned")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        search_item()

    elif choice == "3":
        display_items()

    elif choice == "4":
        return_item()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")