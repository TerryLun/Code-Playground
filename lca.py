class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.val = None


def print_tree(node):
    if not node:
        return
    print_tree(node.left)
    print(node.val)
    print_tree(node.right)


def lca(root, a, b):
    if not root:
        return None
    if root.val == a or root.val == b:
        return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left and right:
        return root
    return left or right


root = Node()
root.val = 4

root.left = Node()
root.left.val = 2

root.right = Node()
root.right.val = 6

root.left.left = Node()
root.left.left.val = 1
root.left.right = Node()
root.left.right.val = 3

root.right.left = Node()
root.right.left.val = 5
root.right.right = Node()
root.right.right.val = 7

node = lca(root, 1, 7)
print(node.val)
