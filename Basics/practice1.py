# Queue using list (basic version)

queue = []
MAX = 5

def enqueue(x):
    if len(queue) == MAX:
        print("Queue Overflow")
    else:
        queue.append(x)
        print("Inserted:", x)

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        x = queue.pop(0)
        print("Deleted:", x)

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)


# main program
while True:
    print("\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Enter value: "))
        enqueue(x)

    elif ch == 2:
        dequeue()

    elif ch == 3:
        display()

    elif ch == 4:
        print("Exit")
        break

    else:
        print("Invalid choice")