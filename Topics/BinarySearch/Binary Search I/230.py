# Definition for a binary tree node.

# This solution is not optimal 
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def find(root):
            if root:
                find(root.left)
                find(root.right)
                ans.append(root.val)
                
        find(root)
        ans.sort()
        print(ans)
        return ans[k - 1]

# optimal one I will choose the:
# least val of node:by inorder traverse left -> root -> right
# This is optimal one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        # if
        def find(root):
            if len(ans) >= k: return
            if root:
                find(root.left)
                ans.append(root.val)
                find(root.right)
                
        find(root)
        # print(ans,ans[-1], ans[k-1])
        return ans[k-1]
