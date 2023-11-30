from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        self.ans = 0
        
        def maxSum(root):
            if not root:
                return True, [-float('inf'), float('inf')], 0
            
            l, l_range, l_sum = maxSum(root.left)
            r, r_range, r_sum = maxSum(root.right)
            
            if l and r and l_range[0] < root.val < r_range[1]:
                total = l_sum + r_sum + root.val
                self.ans = max(self.ans, total)
                return True, [max(r_range[0], root.val), min(l_range[1], root.val)], total
            
            return False, [-float('inf'), float('inf')], 0
        
        maxSum(root)
        return self.ans