# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_depth = 0

        def max_node(root, depth):
            nonlocal max_depth
            if root:
                max_depth = max(depth + 1, max_depth)
                max_node(root.left, depth + 1 )
                max_node(root.right, depth + 1)
            return max_depth

        def pass_node(root):
            if root:
                nonlocal ans, max_depth
                ans1 = ans2 = 0
                max_depth = 0
                if root.left:
                    ans1 = max_node(root.left, 0)
                max_depth = 0
                if root.right:
                    ans2 = max_node(root.right, 0)
                print(ans1, ans2)
                pass_node(root.left)
                pass_node(root.right)
                ans = max(ans, ans1 + ans2)
        pass_node(root)
        return ans


root = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(1)





# [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]  => 8

# root = TreeNode(4)

# root.left = TreeNode(-7)
# root.right = TreeNode(-3)

# root.right.left = TreeNode(-9)
# root.right.right = TreeNode(-9)

# root.right.left.left = TreeNode(9)
# root.right.left.right = TreeNode(-7)

# root.right.left.left.left = TreeNode(6)
# root.right.left.left.left.left = TreeNode(0)
# root.right.left.left.left.right = TreeNode(6)

# root.right.left.left.left.left.right = TreeNode(-1)
# root.right.left.left.left.right.left = TreeNode(6)


# root.right.left.right.left = TreeNode(-6)
# root.right.left.right.right = TreeNode(-6)

# root.right.left.right.left.left = TreeNode(5)

# root.right.left.right.right.left = TreeNode(-9)
# root.right.left.right.right.left.left = TreeNode(2)


slv = Solution()
print(slv.diameterOfBinaryTree(root))
