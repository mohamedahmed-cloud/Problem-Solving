# Definition for a binary tree node.
from typing import Optional
from heapq import heapify, heappop, heappush
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        arr = []
        heapify(arr)
        n = 0

        def dfs(root):
            nonlocal n
            if root:
                if n >= 2 and root.val < -arr[0] and -root.val not in arr:
                    heappop(arr)
                    heappush(arr, -root.val)

                elif n < 2 and -root.val not in arr:
                    heappush(arr, -root.val)
                    n += 1

                dfs(root.left)
                dfs(root.right)

        dfs(root)
        # print(arr)
        return -arr[0] if n ==2 else -1

root = TreeNode(1)

# Build the binary tree by attaching child nodes
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(3)
root.right.left.left = TreeNode(8)
root.right.left.right = TreeNode(4)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(3)
root.left.left.left.left = TreeNode(1)
root.left.left.left.right = TreeNode(6)
root.left.right.right.left = TreeNode(2)
root.left.right.right.right = TreeNode(1)

slv = Solution()
print(slv.findSecondMinimumValue(root))