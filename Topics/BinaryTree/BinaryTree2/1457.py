# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        res = defaultdict(int)

        def dfs(root, nums):
            if root:
                nums[root.val] += 1
                dfs(root.left, nums.copy())
                dfs(root.right, nums.copy())
                if not root.left and not root.right:
                    odd = 0

                    for key, value in nums.items():
                        # print(value)
                        if value % 2 == 1: odd += 1
                    # print(odd)
                    if odd <= 1:
                        self.ans += 1
                        
        dfs(root, res)
        # print(self.ans)
        return self.ans

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)

root.left.left = TreeNode(3)
root.left.right = TreeNode(1)

root.right.right = TreeNode(1)

slv = Solution()
print(slv.pseudoPalindromicPaths(root))