# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # we will make two dfs one for curr node to low
        # second for path curr node to the first dfs
        diff = -float("inf")
        def get_max_difference(node, mn, mx):
            nonlocal diff
            if node:
                mx = max(mx, node.val)
                mn = min(mn, node.val)
                diff = max(diff, abs(mx - mn))
                get_max_difference(node.left, mn, mx)
                get_max_difference(node.right, mn, mx)

        get_max_difference(root, float("inf"), -float("inf"))
        return diff

slv = Solution()
root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

root.right = TreeNode(10)
root.right.right =  TreeNode(14)
root.right.right.left = TreeNode(13)

print(slv.maxAncestorDiff(root))
