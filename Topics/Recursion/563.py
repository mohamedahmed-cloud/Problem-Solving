# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def find(root):

            nonlocal ans

            if not root:
                return 0
                
            left = find(root.left)
            right = find(root.right)

            ans += abs(left - right)

            return left + right + root.val
        
        find(root)
        return ans
