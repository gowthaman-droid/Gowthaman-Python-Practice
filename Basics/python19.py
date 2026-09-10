class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

root = Node(10)
root.right = Node(80)
root.right.left = Node(40)
root.right.left.left = Node(20)
root.right.left.right = Node(50)
root.right.left.left.right = Node(30)
root.right.left.right.right = Node(60)
root.right.left.right.right.right = Node(70)

print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)
print("\nPostorder:")
postorder(root)