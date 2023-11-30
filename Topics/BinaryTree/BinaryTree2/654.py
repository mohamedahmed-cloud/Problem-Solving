# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for curr in nums:
            curr_node = TreeNode(curr)
            while stack and stack[-1].val < curr:
                curr_node.left = stack.pop()
            if stack:
                stack[-1].right = curr_node
            stack.append(curr_node)


        return stack[0]
