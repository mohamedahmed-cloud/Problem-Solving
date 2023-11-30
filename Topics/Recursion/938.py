# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        sum = 0
        def traverse(root):
            nonlocal sum
            if root.left:
                traverse(root.left)
                
            sum += root.val if root.val >= low and root.val <= high else 0

            if root.right:
                traverse(root.right)
        
        traverse(root)
        return sum