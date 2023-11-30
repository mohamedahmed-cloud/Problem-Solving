# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.res = 0, None

        def dfs(root, row):
            if root:
                l = dfs(root.left, row + 1)
                r = dfs(root.right, row + 1)
                # Very important thing this is a technique to capture left & right & it's root
                # in the same time.

                if l[0] == r[0]: return l[0] + 1, root
                elif l[0] > r[0]: return l[0] + 1, l[1]
                else: return r[0] + 1, r[1]

            return self.res

        return dfs(root, 0)[1]

