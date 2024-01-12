from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adjacent_matrix = self.convert(root, defaultdict(list))
        adjacent = adjacent_matrix[start]
        token = set()
        res = 0
        ans = 0

        def dfs(root, ans):
            nonlocal res
            if len(root) == 1 and token:
                res = max(res, ans)
                return

            token.add(start)

            for i in root:
                if i not in token:
                    token.add(i)
                    dfs(adjacent_matrix[i], ans + 1)

        dfs(adjacent, ans)
        return res


    def convert(self, root, adjacent_matrix):
        if root:
            if root.left:
                adjacent_matrix[root.val].append(root.left.val)
                adjacent_matrix[root.left.val].append(root.val)
            if root.right:
                adjacent_matrix[root.val].append(root.right.val)
                adjacent_matrix[root.right.val].append(root.val)
            self.convert(root.left, adjacent_matrix)
            self.convert(root.right, adjacent_matrix)
        return adjacent_matrix


slv = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)

print(slv.amountOfTime(root, 5))
