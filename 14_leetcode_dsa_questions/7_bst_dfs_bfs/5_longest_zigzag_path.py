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
# Binary Tree (Level Order Build)
# -----------------------------
class BinaryTree:
    def __init__(self):
        self.root = None

    def build_from_level_order(self, values):
        if not values:
            return None

        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1


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
# Longest ZigZag Solution
# -----------------------------
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(node):
            if not node:
                return (-1, -1)

            left = dfs(node.left)
            right = dfs(node.right)

            left_len = left[1] + 1     # go left → came from right
            right_len = right[0] + 1   # go right → came from left

            self.max_len = max(self.max_len, left_len, right_len)

            return (left_len, right_len)

        dfs(root)
        return self.max_len


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
tree = BinaryTree()

# LeetCode Example Tree
tree.build_from_level_order(
    [1, None, 1, 1, 1, None, None, 1, 1, None, 1]
)

print("Tree Level Order:")
display_tree(tree.root)

obj = Solution()
result = obj.longestZigZag(tree.root)

print("Longest ZigZag Path Length:", result)
