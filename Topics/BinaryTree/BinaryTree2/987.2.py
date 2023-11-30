# Definition for a binary tree node.
from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = defaultdict(list)            
        def dfs(root, col, row):
            if root:
                vertical[(row, col)].append(root.val)
                dfs(root.left, col -1, row + 1)
                dfs(root.right, col + 1, row + 1)
        dfs(root, 0, 0)
        ans = sorted(vertical.items(), key=lambda x:(x[0][1], x[0][0]))
        print(ans)
        ans = [(x[0][1] ,sorted(x[1])) for x in ans]

        final_dict = defaultdict(list)
        for i in ans:
            final_dict[i[0]].extend(i[1])
        
        ans = [value for key,value in final_dict.items()]
        print(ans)
        return ans

slv = Solution()
root = TreeNode(0)
root.left = TreeNode(8)


root.right = TreeNode(1)
root.right.left = TreeNode(3)
root.right.left.right = TreeNode(4)
root.right.left.right.right = TreeNode(7)
root.right.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.left.left = TreeNode(6)
slv.verticalTraversal(root)
