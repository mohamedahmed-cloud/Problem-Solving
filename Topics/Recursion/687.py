# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def find(root):
            nonlocal ans

            if not root: return 0

            left = find(root.left)
            right = find(root.right)

            Lm = 0
            Rm = 0

            if (root.left and root.left.val == root.val):
                Lm = left + 1
            
            if (root.right and root.right.val == root.val):
                Rm = right + 1
            
            ans = max(ans, Lm + Rm)
            return max(Lm, Rm)

        find(root)

        return ans
