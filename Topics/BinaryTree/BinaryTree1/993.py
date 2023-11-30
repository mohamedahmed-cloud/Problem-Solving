# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth_dic = {"x_parent": 0, "x":0, "y_parent":0, "y": 0}
        prev = 0
        def dfs(root,parent, depth):
            nonlocal prev
            if root:
                if root.val == x:
                    depth_dic["x_parent"] = parent.val
                    depth_dic["x"] = depth

                if root.val == y:
                    depth_dic["y_parent"] = parent.val
                    depth_dic["y"] = depth

                dfs(root.left,root, depth + 1)
                dfs(root.right,root, depth + 1)

        dfs(root,root, 0)
        # print(depth_dic)
        if depth_dic["x_parent"] != depth_dic["y_parent"] and depth_dic["x"] == depth_dic["y"]:
            return True
        return False

