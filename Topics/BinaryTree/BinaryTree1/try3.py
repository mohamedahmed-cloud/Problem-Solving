from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(root):
            if not root:
                return True, [float("inf"), -float("inf")], 0

            l, l_range, l_sum = dfs(root.left)
            r, r_range, r_sum = dfs(root.right)
            if l and r and l_range[1] < root.val < r_range[0]:
                total = r_sum + l_sum + root.val
                self.ans = max(self.ans, total)
                return True, [min(l_range[0], root.val), max(r_range[1], root.val)], total

            return False, [float("inf"), -float("inf")], None
        dfs(root)
        return self.ans

root = TreeNode(20)
root.left = TreeNode(4)
root.right = TreeNode(5)
slv = Solution()
print(slv.maxSumBST(root))