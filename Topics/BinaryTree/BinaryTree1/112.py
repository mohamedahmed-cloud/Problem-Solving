# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, currSum, targetSum):
            if root:
                currSum += root.val
                print(currSum)
                if currSum == targetSum and (not root.left and not root.right ):
                    return True
                return dfs(root.left, currSum , targetSum) or dfs(root.right, currSum, targetSum)

        return dfs(root, 0, targetSum)