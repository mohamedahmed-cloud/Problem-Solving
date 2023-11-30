# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dictionary = defaultdict(int)

        def dfs(root):
            if root:
                dictionary[str(root.val)] += 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        dictionary = sorted(dictionary.items(), key = lambda x: -x[1])
        n = len(dictionary)
        result = {int(dictionary[0][0])}
        mx = int(dictionary[0][1])
        for i in range(1, n):
            if mx == dictionary[i][1]:
                result.add(int(dictionary[i][0]))
        return result
slv = Solution()
root = TreeNode(1)
root.right = TreeNode(1)
root.left = TreeNode(2)
root.right.left = TreeNode(2)
print(slv.findMode(root))
