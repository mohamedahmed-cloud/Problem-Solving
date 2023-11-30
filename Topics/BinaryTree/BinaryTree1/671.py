# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l = deque([float("inf"), float("inf")])
        def dfs(root):
            if root:
                value = root.val
                for i in range(2):
                    if value < l[i]:
                        if i == 0:
                            l[1] = l[0]
                        if i == 1 and value == l[0]:
                            break
                        l[i] = value
                        break
                dfs(root.left)
                dfs(root.right)


        dfs(root)
        print(l)
        return l[1] if l[1] != l[0] and l[1] != float("inf") else -1