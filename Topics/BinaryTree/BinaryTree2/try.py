from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, mx, mn):
            nonlocal ans
            if root:
                ans = max(ans, abs(mx - root.val), abs(mn - root.val))
                # print(abs(mx - root.val))
                dfs(root.left, max(mx, root.val), min(mn, root.val))
                dfs(root.right, max(mx, root.val), min(mn, root.val))
                
        dfs(root, root.val, root.val)
        return ans

slv = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(0)
root.left.left.right = TreeNode(3)

print(slv.maxAncestorDiff(root))
