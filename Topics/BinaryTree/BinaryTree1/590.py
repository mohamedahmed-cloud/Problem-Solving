from typing import Optional, List
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = deque()

        def dfs(root):
            if not root:
                return None
            for child in root.children:
                dfs(child)
            res.append(root.val)
            
        dfs(root)
        return res
            