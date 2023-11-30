# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        res = defaultdict(int)
        def dfs(root, row):
            if root:
                res[row] += root.val
                dfs(root.left, row  + 1)
                dfs(root.right, row + 1)
        dfs(root, 0)
        ans = 0
        max_element = -float("inf")
        for key, value in res.items():
            if value > max_element:
                max_element = value
                ans = key
        return ans + 1