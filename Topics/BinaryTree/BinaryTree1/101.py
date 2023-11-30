# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        lleft = []
        lright = []
        def dfs(root):
            if root:
                lleft.append(root.val)
                dfs(root.left)
                dfs(root.right)
            lleft.append(None)
        dfs(root.left)

        def dfs2(root):
            if root:
                lright.append(root.val)
                dfs2(root.right)
                dfs2(root.left)
            lright.append(None)
        dfs2(root.right)
        
        return lright == lleft

# Another Good Solution.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2:
                return False
            elif r1.val != r2.val:
                return False
            
            return dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
        return dfs(root.left, root.right) 