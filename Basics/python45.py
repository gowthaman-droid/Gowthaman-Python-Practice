#develop a lib management sysytem to manage book records and librry members and book searchs and borrowing satus the system should allwo the librainan to update delte and display the book reord ,search for book by isbn no. or title using a apropriate searching algorithm and also sort books by title publication year using a sorting algorthim,manage the books issue under return transaction using a queue and maintain the borrrowing history using the linked list,use the stack to undo themost recent trasanctionand organsise the books catagory using a binary tree with sutiable traversal operation from the develop the application using a menu driven interface and demostrate acorrect funtion of each opertion with sample data and then a database 

books = [
    ["101", "Python Basics", "John", 2022, "Programming", "Available"],
    ["102", "Data Structures", "James", 2021, "Programming", "Available"],
    ["103", "Database Systems", "Peter", 2023, "Database", "Available"]
]

members = [["M01", "Gowtham"], ["M02", "Arun"]]
queue = []
stack = []
history = None
root = None


def add_book():
    isbn = input("ISBN: ")
    for b in books:
        if b[0] == isbn:
            print("ISBN already exists")
            return
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    category = input("Category: ")
    books.append([isbn, title, author, year, category, "Available"])
    print("Book added")


def display_books():
    for b in books:
        print(b)


def update_book():
    isbn = input("ISBN to update: ")
    for b in books:
        if b[0] == isbn:
            b[1] = input("New title: ")
            b[2] = input("New author: ")
            b[3] = int(input("New year: "))
            b[4] = input("New category: ")
            print("Book updated")
            return
    print("Book not found")


def delete_book():
    isbn = input("ISBN to delete: ")
    for b in books:
        if b[0] == isbn:
            if b[5] == "Issued":
                print("Return the book before deleting")
                return
            books.remove(b)
            print("Book deleted")
            return
    print("Book not found")


def search_book():
    key = input("Enter ISBN or title: ").lower()
    found = False
    for b in books:
        if key == b[0].lower() or key in b[1].lower():
            print(b)
            found = True
    if not found:
        print("Book not found")


def sort_books():
    print("1. Title")
    print("2. Publication year")
    choice = input("Choose: ")
    index = 1 if choice == "1" else 3

    for i in range(len(books)):
        for j in range(len(books) - i - 1):
            if books[j][index] > books[j + 1][index]:
                books[j], books[j + 1] = books[j + 1], books[j]

    display_books()


def add_member():
    mid = input("Member ID: ")
    for m in members:
        if m[0] == mid:
            print("Member already exists")
            return
    name = input("Name: ")
    members.append([mid, name])
    print("Member added")


def display_members():
    for m in members:
        print(m)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_history(data):
    global history
    node = Node(data)
    node.next = history
    history = node


def display_history():
    current = history
    while current:
        print(current.data)
        current = current.next


def add_request():
    action = input("Issue or return: ").lower()
    if action not in ["issue", "return"]:
        print("Invalid action")
        return
    isbn = input("ISBN: ")
    mid = input("Member ID: ")
    queue.append([action, isbn, mid])
    print("Request added to queue")


def process_request():
    if not queue:
        print("Queue is empty")
        return

    action, isbn, mid = queue.pop(0)

    book = None
    for b in books:
        if b[0] == isbn:
            book = b

    member_found = False
    for m in members:
        if m[0] == mid:
            member_found = True

    if book is None or not member_found:
        print("Invalid book or member")
        return

    if action == "issue" and book[5] == "Available":
        book[5] = "Issued"
    elif action == "return" and book[5] == "Issued":
        book[5] = "Available"
    else:
        print("Transaction not allowed")
        return

    transaction = [action, isbn, mid]
    stack.append(transaction)
    add_history(transaction)
    print("Transaction completed")


def undo_transaction():
    if not stack:
        print("Nothing to undo")
        return

    action, isbn, mid = stack.pop()

    for b in books:
        if b[0] == isbn:
            if action == "issue":
                b[5] = "Available"
            else:
                b[5] = "Issued"
            print("Transaction undone")
            return


class Category:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_category(node, value):
    if node is None:
        return Category(value)
    if value < node.value:
        node.left = insert_category(node.left, value)
    elif value > node.value:
        node.right = insert_category(node.right, value)
    return node


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)


def build_tree():
    global root
    root = None
    for b in books:
        root = insert_category(root, b[4])


def show_categories():
    build_tree()
    print("1. Inorder")
    print("2. Preorder")
    print("3. Postorder")
    choice = input("Choose: ")

    if choice == "1":
        inorder(root)
    elif choice == "2":
        preorder(root)
    elif choice == "3":
        postorder(root)
    else:
        print("Invalid choice")


while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Display books")
    print("5. Search book")
    print("6. Sort books")
    print("7. Add member")
    print("8. Display members")
    print("9. Add issue/return request")
    print("10. Process request")
    print("11. Borrowing history")
    print("12. Undo transaction")
    print("13. Category tree traversal")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        search_book()
    elif choice == "6":
        sort_books()
    elif choice == "7":
        add_member()
    elif choice == "8":
        display_members()
    elif choice == "9":
        add_request()
    elif choice == "10":
        process_request()
    elif choice == "11":
        display_history()
    elif choice == "12":
        undo_transaction()
    elif choice == "13":
        show_categories()
    elif choice == "0":
        print("Exiting library system")
        break
    else:
        print("Invalid choice")
