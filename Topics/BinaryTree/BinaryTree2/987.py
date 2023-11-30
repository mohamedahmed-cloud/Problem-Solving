# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = 0
        # In this problem we will have a two dfs function
        # First to pass each node to second dfs function
        # second dfs function calculate average of this node
        def get_average(root, value, passed_value):
            if root:
                value[0] += root.val
                value[1] += 1
                get_average(root.left, value, passed_value)
                get_average(root.right, value, passed_value)
            return passed_value == value[0] // value[1]

        def dfs(root):
            if root:
                self.ans += get_average(root, [0, 0], root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        print(self.ans)
        return self.ans