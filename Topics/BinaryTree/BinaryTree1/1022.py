# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, path):
            if not node: return 0

            path += str(node.val)

            if not node.left and not node.right:
                return int(path, 2)
            
            return dfs(node.left, path) + dfs(node.right, path)
            
        return dfs(root, "")

root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right= TreeNode(1)
root.right= TreeNode(1)
root.right.left= TreeNode(0)
root.right.right= TreeNode(1)

slv = Solution()
print(slv.sumRootToLeaf(root))
