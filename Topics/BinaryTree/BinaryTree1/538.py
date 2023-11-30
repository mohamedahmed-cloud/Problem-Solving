# Definition for a binary tree node.
from typing import Optional, List
import bisect
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        l = deque()
        n = 0
        def dfs(root):
            nonlocal n
            if root:
                l.append(root.val)
                dfs(root.right)
                dfs(root.left)
                n += 1

        dfs(root)
        l = sorted(l)
        res = [0] * (n + 1)
        cnt = 1

        for i in range(n - 1, -1, -1):
            res[cnt] += res[cnt -1] + l[i]
            cnt += 1

        def dfs(root):
            if root:
                currIndex = bisect.bisect_right(l, root.val)
                root.val = res[-currIndex]
                dfs(root.left)
                dfs(root.right)
                return root
        return dfs(root)

def print_root(root):
    if root:
        print(root.val)
        print_root(root.left)
        print_root(root.right)
root = TreeNode(12)
root.left = TreeNode(13)
root.right = TreeNode(14)
root.right.left = TreeNode(1)
slv = Solution()
slv.convertBST(root)
print_root(root)

