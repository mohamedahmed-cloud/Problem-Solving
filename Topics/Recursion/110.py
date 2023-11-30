# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def find(root):
            if not root:
                return 0

            l = find(root.left)
            if l is False:return False

            r = find(root.right)
            if r is False:return False

            if abs(l - r) > 1:
                return False

            return max(l,r) + 1

        ans = find(root)

        return ans != False