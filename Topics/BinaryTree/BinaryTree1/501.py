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
                dictionary[root.val] += 1
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        l = sorted(list(dictionary.items()),key= lambda x : x[1], reverse=True)
        # print(l)
        # ans = [l[0]]
        res = set([l[0][0]])
        for i in l[1:]:
            if i[-1] == l[0][-1]:
                res.add(i[0])
                continue
            break

        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
root.right.right = TreeNode(1)
slv = Solution()
print(slv.findMode(root))
