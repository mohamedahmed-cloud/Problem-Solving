# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        
        def find(root):
            if root:
                find(root.left)
                find(root.right)
                ans.append(root.val)
        find(root)
        return ans