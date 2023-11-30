from typing import Optional, List
# Definition for a Node.

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root:return []

        res = [root.val]
        def dfs(root):
            if not root: return None

            # res.append(root.val)

            for child in root.children if root.children else []:
                res.append(child.val)
                dfs(child)

        dfs(root)
        return res
    
# root = Node(1)
# root.children = [Node(2), Node(3), Node(4)]
# root.children[0].children = [Node(5), Node(6)]
# slv = Solution()
# print(slv.preorder(root))