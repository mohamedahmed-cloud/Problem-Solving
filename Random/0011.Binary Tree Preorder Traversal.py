#    Author : Mohamed Yousef 
#    Date   : 2023-01-09
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.output=[]
        def traversal(root):
            if root:
                self.output.append(root.val)
                traversal(root.left)
                traversal(root.right)
        traversal(root)
        return self.output

