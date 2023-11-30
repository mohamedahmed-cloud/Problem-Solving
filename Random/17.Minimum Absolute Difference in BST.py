# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans=[]
        def dfs(root):
            if root:
                dfs(root.right)
                ans.append(root.val)
                dfs(root.left)
        dfs(root)
        n=len(ans)
        res=float(inf)
        for i in range(1,n):
            res=min(ans[i-1]-ans[i],res)
        print(ans)
        return res