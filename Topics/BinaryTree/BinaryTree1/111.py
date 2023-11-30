# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans = float("inf")

        def dfs(root, currDepth):
            nonlocal ans
            if root:
                dfs(root.left, currDepth + 1)
                dfs(root.right, currDepth + 1)
                if root and not root.left and not root.right:
                    ans = min(ans, currDepth)
        
        dfs(root, 0)
        return ans + 1 if ans != float("inf") else 0

