# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preorder, postorder):
            if not preorder or not postorder:
                return None

            curr_val = postorder.pop()
            root = TreeNode(curr_val)
            stack = []

            while preorder[-1] != postorder[-1]:
                stack.append(preorder.pop())
                

        
def dfs(root):
    if root:
        print(root.val)
        dfs(root.left)
        dfs(root.right)
