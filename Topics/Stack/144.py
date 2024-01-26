# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: list) -> List[int]:
        
        ans = []


        def find(root):
            if root:
                ans.append(root.val)
                if root.left:
                    find(root.left)
                if root.right:
                    find(root.right)
            
        find(root)
        return ans