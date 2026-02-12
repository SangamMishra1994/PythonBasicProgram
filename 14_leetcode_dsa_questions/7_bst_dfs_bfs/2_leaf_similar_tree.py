from typing import Optional, List
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
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert node level-wise (like LeetCode input)
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


# -------------------------
# Solution Class
# -------------------------
class Solution2:
    def leafSimilar(
        self,
        root1: Optional[TreeNode],
        root2: Optional[TreeNode]
            ) -> bool:
        list1 = []
        list2 = []

        self.helper_function(root1, list1)
        self.helper_function(root2, list2)

        return list1 == list2

    def helper_function(self, root: Optional[TreeNode], leaves: List[int]):
        if root is None:
            return

        if root.left is None and root.right is None:
            leaves.append(root.val)

        self.helper_function(root.left, leaves)
        self.helper_function(root.right, leaves)


# -------------------------
# Driver Code
# -------------------------

# Create first tree
tree1 = BinaryTree()
tree1.insert(3)
tree1.insert(5)
tree1.insert(1)
tree1.insert(6)
tree1.insert(2)
tree1.insert(9)
tree1.insert(8)

# Create second tree
tree2 = BinaryTree()
tree2.insert(3)
tree2.insert(5)
tree2.insert(1)
tree2.insert(6)
tree2.insert(7)
tree2.insert(4)
tree2.insert(2)
tree2.insert(9)
tree2.insert(8)

# Check leaf similarity
solution = Solution2()
result = solution.leafSimilar(tree1.root, tree2.root)

print("Leaf Similar Trees:", result)
