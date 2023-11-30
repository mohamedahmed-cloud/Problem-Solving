# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        Sum = [(0, 0)] * (10 ** 4 + 1)

        def dfs(root, level , times , Sum ):
            if not root: return 0

            Sum[level] = (root.val+ Sum[level][0], Sum[level][1] + 1)

            dfs(root.left, level + 1, times, Sum)
            dfs(root.right, level + 1, times, Sum)
            return Sum
            
        dfs(root, 0 , 0, Sum)
        ans = []
        for i in Sum:
            if i != (0,0):
                ans.append(round(i[0] / i[1],5))
        return ans