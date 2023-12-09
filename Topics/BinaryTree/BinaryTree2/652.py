from typing import Optional, List
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None, root=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = root
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(int)
        ans = []
        def dfs(root):
            if not root:
                return "N"
            subtree = ",".join([str(root.val), dfs(root.left), dfs(root.right)])
            subtrees[subtree] += 1
            if subtrees[subtree] == 2:
                ans.append(root)
            return subtree
        dfs(root)
        return ans

        

    


# def printd(root):
#     for i in root:
#         print(i.val, "yousf")
#         def dfs(i):
#             if i:
#                 print(i.val)
#                 dfs(root.left)
#                 dfs(root.right)
#         dfs(i)

slv = Solution()
# [1,2,3,4,null,2,4,null,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)
print(slv.findDuplicateSubtrees(root))
