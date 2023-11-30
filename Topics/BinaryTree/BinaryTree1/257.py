# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        curr = ""
        res = []
        def dfs(root, curr):
            if root:
                curr += f"{root.val}->"
                dfs(root.left, curr)
                dfs(root.right, curr)
                if not root.left and not root.right:
                    res.append(curr[:-2])

        dfs(root, curr)
        return res
            