# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if root:
                if (root == p or root == q):
                    return root
                l = dfs(root.left)
                r = dfs(root.right)
                if r and l:
                    return root
                elif l:
                    return l
                elif r: 
                    return r
        return dfs(root)

slv = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
slv.lowestCommonAncestor(root, root.left, root.right)