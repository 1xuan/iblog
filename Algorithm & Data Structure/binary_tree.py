"""
Binary Search Trees
"""

"""
tree_arr = [10, 5, 15, 3, 8, 13, None, None, None, 7, None]
"""

class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.right.left = Node(13)

root.left.left = Node(3)
root.left.right = Node(8)

root.left.right.left = Node(7)


def inorder_tree_walk(root):
    if root:
        inorder_tree_walk(root.left)
        print(root.key)
        inorder_tree_walk(root.right)


def binary_tree_search(root, key):
    if not root or root.key == key:
        return root

    if key < root.key:
        return binary_tree_search(root.left, key)
    else:
        return binary_tree_search(root.right, key)


def binary_tree_iterative_search(root, k):
    while root and root.key != key:
        if key < root.key:
            root = root.left
        else:
            root = root.right

    return root


def tree_minimum(root):
    while root.left:
        root = root.left
    return root


def tree_maximum(root):
    while root.right:
        root = root.right
    return root

"""
Red-Block Tree
"""




