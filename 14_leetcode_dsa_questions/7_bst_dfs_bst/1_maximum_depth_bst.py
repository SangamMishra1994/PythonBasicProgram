from typing import Optional
from collections import deque


# -------------------------
# Tree Node Definition
# -------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------
# Binary Tree Class
# -------------------------
class Solution1:
    def __init__(self):
        self.root = None

    # Insert nodes level-wise (like LeetCode input)
    def insert(self, val):
        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    # Display tree level order
    def display(self):
        if not self.root:
            print("Tree is empty")
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()

    # -------------------------
    # Maximum Depth (LC 104)
    # -------------------------
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


# -------------------------
# Driver Code
# -------------------------
tree = Solution1()

# Insert nodes
tree.insert(3)
tree.insert(9)
tree.insert(20)
tree.insert(15)
tree.insert(7)

# Display tree
print("Binary Tree (Level Order):")
tree.display()

# Find maximum depth
depth = tree.maxDepth(tree.root)

print("Maximum Depth of Binary Tree:", depth)
