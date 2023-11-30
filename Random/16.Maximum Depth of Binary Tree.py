# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,depth):
            if root:
                return max(dfs(root.right,depth+1),dfs(root.left,depth+1))
            return depth
        return dfs(root,0)