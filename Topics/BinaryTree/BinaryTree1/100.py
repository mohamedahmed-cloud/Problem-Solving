# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            def dfs(p, q):
                if p and q:
                    if p.val != q.val:
                        return False

                    left = dfs(p.left,q.left)
                    right = dfs(p.right, q.right)
                    return left and right

                elif (p and not q ) or (not p and q):
                    return False
                else:
                    return True


            return dfs(q, p)

p = TreeNode(1)
p.left = TreeNode(2)

q = TreeNode(1)
p.right = TreeNode(2)

slv = Solution()
print(slv.isSameTree(p,q))
