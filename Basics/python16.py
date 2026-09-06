contacts={}
def add_contact():
    name=input("Enter Name: ")
    phn=input("Enter Phn: ")
    contacts[name]=phn
    print("Comtact added successfully!\n")

def search_contact():
    name=input("Enter name to search: ")
    if name in contacts:
        print(f"{name} -> {contacts[name]}\n")
    else:
        print("Contact not found!")

def delete_contact():
    name=input("Enter name to search: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!\n")
    else:
        print("Contact not found!")

def display_contact():
    if not contacts:
        print("No contacts!")
    else:
        for name,phn in contacts.items():
            print(f"{name} -> {phn}")
        print()

while True:
    print("1. Add contact\n2. Search contact\n3. Delete contact\n4.Display contact\n5. Exit system!")
    ch=int(input("Enter Your choice: "))
    if ch==1:
        add_contact()
    elif ch==2:
        search_contact()
    elif ch==3:
        delete_contact()
    elif ch==4:
        display_contact()
    elif ch==5:
        print("Exiting the contacts!!")
        break
    else:
        print("Enter a valid Choices!!!")