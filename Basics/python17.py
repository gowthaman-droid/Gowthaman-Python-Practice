from collections import deque

queue = deque()

def add_student():
    name = input("Enter student name: ")
    queue.append(name)
    print(f"{name} added to queue\n")

def issue_book():
    if queue:
        student = queue.popleft()
        print(f"Book issued to {student}\n")
    else:
        print("No students in queue\n")

def show_queue():
    print("Queue:", list(queue), "\n")

while True:
    print("1. Add Student")
    print("2. Issue Book")
    print("3. Show Queue")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        issue_book()
    elif choice == '3':
        show_queue()
    elif choice == '4':
        break
    else:
        print("Invalid choice\n")