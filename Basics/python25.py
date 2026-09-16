queue = []
stack = []
answers = {
    "what is python": "Python is a high-level programming language.",
    "what is stack": "Stack is LIFO (Last In First Out) data structure.",
    "what is queue": "Queue is FIFO (First In First Out) data structure.",
    "what is linked list": "Linked list is a linear data structure where elements are connected using pointers.",
    "what is array": "Array is a collection of same type elements stored in continuous memory.",
    "what is tree": "Tree is a non-linear hierarchical data structure with root and nodes.",
    "what is binary tree": "Binary tree is a tree where each node has at most 2 children.",
    "what is bst": "BST is Binary Search Tree where left < root < right.",
    "what is graph": "Graph is a collection of nodes connected by edges.",
    "what is dfs": "DFS is Depth First Search traversal of a graph or tree.",
    "what is bfs": "BFS is Breadth First Search traversal using queue.",
    "what is recursion": "Recursion is a function calling itself.",
    "what is sorting": "Sorting is arranging elements in increasing or decreasing order."
}
while True:
    print("\n1. Ask Question\n2. Show Pending Question \n3. Show Answer History \n4.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        q = input("Ask your question: ").lower()
        if q in answers:
            print("Answer:", answers[q])
            stack.append(q)
        else:
            print("Sorry, I don't know this.")
            queue.append(q)
    elif choice == "2":
        print("Pending Questions:", queue)
    elif choice == "3":
        print("Answered Questions:", stack)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")