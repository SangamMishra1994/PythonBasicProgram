from typing import Optional
from collections import deque


# -----------------------------
# Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# BST Creation
# -----------------------------
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return

        current = self.root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break


# -----------------------------
# Display Tree (Level Order)
# -----------------------------
def display_tree(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


# -----------------------------
# Search in BST Solution
# -----------------------------
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int):
        if not root:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
if __name__ == "__main__":

    # Create BST
    bst = BinarySearchTree()
    values = [4, 2, 7, 1, 3]

    for v in values:
        bst.insert(v)

    print("Original BST (Level Order):")
    display_tree(bst.root)

    # Search value
    search_value = 2
    sol = Solution()
    result = sol.searchBST(bst.root, search_value)

    print(f"\nSearching for value {search_value}")

    if result:
        print("Subtree rooted at", search_value, "(Level Order):")
        display_tree(result)
    else:
        print("Value not found in BST")
