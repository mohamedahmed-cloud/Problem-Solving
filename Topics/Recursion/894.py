# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
            dp = {0:[], 1: [TreeNode()] }
            def find(n):
                if n in dp:
                    return dp[n]
                res = set()
                
                for i in range(1,n, 2):
                    left, right = find(i), find(n-i-1)
                    # print(i,n-i-1)
                    for l in left:
                        for r in right:
                            res.add(TreeNode(0,l,r))
                dp[n] = res
                return list(res)
            return find(n)