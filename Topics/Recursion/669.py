# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            nonlocal low, high
            
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if low <= node.val <= high:
                return node

            elif low > node.val:
                temp = node.right
                node = None
                return temp

            elif high < node.val:
                temp = node.left
                node = None
                return temp

            return node

        root = dfs(root)
        return root
    
x = TreeNode(1)
x.right = TreeNode(2)
slv = Solution()
x = slv.trimBST(x, 2, 4)


def print_node(node):
    if node is not None:
        print(node.val)
        print_node(node.left)
        print_node(node.right)

print_node(x)

# another solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(node):
            nonlocal low, high
            if node:
                if node.val < low:
                    return dfs(node.right)

                elif node.val > high:
                    return dfs(node.left)

                else:
                    node.left = dfs(node.left)
                    node.right = dfs(node.right)

            return node
            
        return dfs(root)


       