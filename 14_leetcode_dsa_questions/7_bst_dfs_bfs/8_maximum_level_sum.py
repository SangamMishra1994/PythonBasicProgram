from typing import Optional, List
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
# Binary Tree Builder
# (Build from LeetCode level order list)
# -----------------------------
class BinaryTree:
    def __init__(self):
        self.root = None

    def build_from_level_order(self, values: List[Optional[int]]):
        if not values:
            return None

        self.root = TreeNode(values[0])
        queue = deque([self.root])
        i = 1

        while queue and i < len(values):
            node = queue.popleft()

            # Left child
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1

            # Right child
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
# Solution
# -----------------------------
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 1

        while queue:
            level_size = len(queue)
            current_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                current_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Update max level
            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level

            level += 1

        return max_level


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
if __name__ == "__main__":

    # LeetCode Example
    root_values = [1, 7, 0, 7, -8, None, None]

    tree = BinaryTree()
    tree.build_from_level_order(root_values)

    print("Tree (Level Order):")
    display_tree(tree.root)

    sol = Solution()
    result = sol.maxLevelSum(tree.root)

    print("Maximum Level Sum occurs at Level:", result)
