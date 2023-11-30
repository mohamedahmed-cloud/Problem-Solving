# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        ans = float('inf')
        prev = float('inf')

        def traversal(root):

            nonlocal ans, prev

            if root.left:
                traversal(root.left)

            ans = min(abs(prev - root.val), ans)
            prev = root.val

            if root.right:
                traversal(root.right)
            # print(ans)

        traversal(root)
        return ans