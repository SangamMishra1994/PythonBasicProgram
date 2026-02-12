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
# LCA Solution (LeetCode 236)
# -----------------------------
class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:

        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right


# -----------------------------
# Helper: Find Node by Value
# -----------------------------
def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
if __name__ == "__main__":

    # Build tree (same as LeetCode example)
    tree = BinaryTree()
    tree.build_from_level_order([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

    print("Tree (Level Order):")
    display_tree(tree.root)

    # Nodes to find LCA for
    p_val = 5
    q_val = 4

    p = find_node(tree.root, p_val)
    q = find_node(tree.root, q_val)

    sol = Solution()
    lca = sol.lowestCommonAncestor(tree.root, p, q)

    print(f"LCA of {p_val} and {q_val} is:", lca.val)
