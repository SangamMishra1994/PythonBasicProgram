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
# Binary Tree (Level Order Build)
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
# Right Side View Solution
# -----------------------------
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # last node at each level
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
if __name__ == "__main__":

    tree = BinaryTree()
    tree.build_from_level_order([1, 2, 3, None, 5, None, 4])

    print("Tree (Level Order):")
    display_tree(tree.root)

    sol = Solution()
    result = sol.rightSideView(tree.root)

    print("Right Side View:", result)
