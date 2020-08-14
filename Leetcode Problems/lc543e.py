"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameterOfBinaryTree(root):
    res = 0

    def dfs(node):
        if not node:
            return 0
        nonlocal res
        left = dfs(node.left)
        right = dfs(node.right)
        res = max(res, left + right)
        return max(left, right) + 1

    dfs(root)
    return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(diameterOfBinaryTree(root))
