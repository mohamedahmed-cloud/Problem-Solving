# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # find depth for each node

        depth = {None: 0}
        def dfs(node, parent):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root, None)
        maxdepth = max(depth.values())
        # print( maxdepth)
        # find the specific node
        def find(node):
            if not node:
                return None
            if maxdepth == depth[node]:
                return node
            l, r = find(node.left), find(node.right)
            
            return node if l and r else l or r

        return find(root)
           
        
        