from collections import deque


# -----------------------------
# Tree Node
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
# Delete Node Solution
# -----------------------------
class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return root

        if root.val == key:

            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is not None and root.right is None:
                return root.left

            if root.left is None and root.right is not None:
                return root.right

            # Case 3: Two children
            min_node = self.findMinValue(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
            return root

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root

    def findMinValue(self, root):
        temp = root
        while temp.left:
            temp = temp.left
        return temp


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
if __name__ == "__main__":

    bst = BinarySearchTree()
    values = [5, 3, 6, 2, 4, 7]

    for v in values:
        bst.insert(v)

    print("Original BST (Level Order):")
    display_tree(bst.root)

    delete_key = 3
    sol = Solution()
    bst.root = sol.deleteNode(bst.root, delete_key)

    print(f"\nBST after deleting {delete_key}:")
    display_tree(bst.root)
