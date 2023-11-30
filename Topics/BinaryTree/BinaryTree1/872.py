# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, ans):
            if not root: return 0
            if not root.left and not root.right: ans.append(root.val)
            dfs(root.left, ans)
            dfs(root.right, ans)
            return ans

        ans1 = dfs(root1, [])
        ans2 = dfs(root2, [])
        if ans1 == ans2:
            return True
        return False