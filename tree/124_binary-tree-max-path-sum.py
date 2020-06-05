# Given a non-empty binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_value = 0

    def maxPathSum(self, root: TreeNode) -> int:
        def pathSum(node):
            if node == None:
                return 0
            left = max(0, pathSum(node.left))
            right = max(0, pathSum(node.right))
            self.max_value = max(self.max_value, left + right + node.val)
            print(node.val, left, right)
            return max(left, right) + node.val

        pathSum(root)
        return self.max_value