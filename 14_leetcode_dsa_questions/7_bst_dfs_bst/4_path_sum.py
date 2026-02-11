from typing import Optional
from collections import defaultdict, deque


# -----------------------------
# Tree Node Definition
# -----------------------------
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# BST Creation from User Input
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

            if values[i] is not None:
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
# Path Sum III Solution
# -----------------------------
class Solution4:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, currentSum):
            if not node:
                return 0

            currentSum += node.val
            count = prefix[currentSum - targetSum]

            prefix[currentSum] += 1
            count += dfs(node.left, currentSum)
            count += dfs(node.right, currentSum)
            prefix[currentSum] -= 1

            return count

        return dfs(root, 0)


# -----------------------------
# MAIN DRIVER CODE
# -----------------------------
tree1 = BinaryTree()
tree1.build_from_level_order([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])

targetSum = 8
obj = Solution4()
result = obj.pathSum(tree1.root, targetSum)

print("Number of paths with sum", targetSum, ":", result)
