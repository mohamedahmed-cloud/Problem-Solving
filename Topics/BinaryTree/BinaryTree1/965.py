# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        s = root.val
        ans1 = 0
        ans2 = 0
        def dfs(root):

            if not root:
                return True 
            if s != root.val:  return False
            ans1 =  dfs(root.left)
            ans2 = dfs(root.right)

            return ans1 and ans2

        return dfs(root)
