from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        def dfs(root):
            nonlocal ans
            if root:
                ans += str(root.val)
                if root.left:
                    ans += "("
                if not root.left and root.right:
                    ans += "()"
                dfs(root.left)
                if root.right:
                    ans += "("
                dfs(root.right)
                ans += ")"
        dfs(root)
        return ans[:-1]
slv = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
print(slv.tree2str(root))