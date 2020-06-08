# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
# Return true if and only if the nodes corresponding to the values x and y are cousins.

# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def bfs(node: TreeNode, parent: TreeNode, height: int, value: int):
            if node:
                if node.val != value:
                    return bfs(node.left, node, height + 1, value) or bfs(
                        node.right, node, height + 1, value)
                else:
                    return height, parent

        depth1, parent1 = bfs(root, None, 0, x)
        depth2, parent2 = bfs(root, None, 0, y)
        print(depth1, depth2, parent1, parent2)
        return depth1 == depth2 and parent1 != parent2
