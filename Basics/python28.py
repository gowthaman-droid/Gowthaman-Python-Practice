class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
print(height(root))