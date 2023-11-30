# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        def valid(node, left, right):
            if not node: return True
        

            if not (node.val > left and node.val < right):
                return False
        
            x  = valid(node.left, left, node.val) 
            y = valid(node.right, node.val, right)

            return x and y
            
        return valid(root, - float("inf"), float('inf'))