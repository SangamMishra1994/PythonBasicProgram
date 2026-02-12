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
class Solution3:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0

            # Update max for the path
            new_max = max(max_so_far, node.val)

            return good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, root.val)
    

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


# Check leaf similarity
solution = Solution3()
result = solution.goodNodes(tree1.root)

print("Total Good Nodes are:", result)
