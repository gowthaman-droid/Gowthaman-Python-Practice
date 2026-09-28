stack = []

def push(item):
    stack.append(item)
    print(item, "pushed into stack")


def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        item = stack.pop()
        print(item, "popped from stack")


def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Top element:", stack[-1])


def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack elements:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

push(10)
push(20)
push(30)
display()
peek()
pop()
display()