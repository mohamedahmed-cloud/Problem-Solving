# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = set()
        def dfs(root):
            if root:
                nums.add(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)    
        for i in nums:
            if (k - i) in nums and (k - i) != i:
                return True
        return False

        