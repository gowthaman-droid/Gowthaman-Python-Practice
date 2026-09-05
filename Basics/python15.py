def reverse_queue(q):
    stack=[]
    while q:
        stack.append(q.pop(0))
    while stack:
        q.append(stack.pop())
    return q
q=list(map(int,input("Enter the elements: ").split()))
print(reverse_queue(q))