# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return 

        ans = []    

        def traverse(root):
            if root.left:
                traverse(root.left)

            ans.append(root.val)

            if root.right:
                traverse(root.right)
            return ans

        return traverse(root)