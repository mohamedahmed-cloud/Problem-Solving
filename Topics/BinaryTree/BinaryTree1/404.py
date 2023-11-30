# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans =[0]
        def dfs(root):
            if root:
                if root.left and (root.left.left is None and root.left.right is None):
                    ans[0] += root.left.val
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ans[0]
