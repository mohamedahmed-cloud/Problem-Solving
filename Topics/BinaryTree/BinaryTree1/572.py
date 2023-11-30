# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def slv(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2:
                return False
            
            elif r1.val != r2.val:
                return False
            
            return slv(r1.left, r2.left) and slv(r1.right, r2.right)


        def dfs(root, subRoot):
            if root:
                if root.val == subRoot.val:
                    ans = slv(root, subRoot)
                    if ans:return ans
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
