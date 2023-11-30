# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def dfs( inorder, postorder):
            if not inorder or not postorder:
                return None

            curr_val = postorder.pop()
            root = TreeNode(curr_val)
            mid = inorder.index(curr_val)

            root.left = dfs(inorder[:mid], postorder[: mid])
            root.right = dfs(inorder[mid + 1:], postorder[mid :])

            return root

        return dfs(inorder, postorder)