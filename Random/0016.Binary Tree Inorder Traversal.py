#    Author : Mohamed Yousef 
#    Date   : 2023-01-13
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output=[]
        def inorder(root):
            if root:
                inorder(root.left)
                self.output.append(root.val)    
                inorder(root.right)
        inorder(root)
        return self.output
