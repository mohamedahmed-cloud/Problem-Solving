# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
     
        def dfs(root):
            nonlocal p, q
            if root:
                if root.val > q.val and root.val > p.val:
                    return dfs(root.left)
                elif root.val < q.val and root.val < p.val:
                    return dfs(root.right)
                else:
                    return root
        return dfs(root)
