# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        # We will solve using BFS
        queue = [(original, cloned)]

        while queue:
            origin, clone = queue.pop(0)
            # print(origin, clone)
            if origin == target:
                return clone
            if origin.left:
                queue.append((origin.left,clone.left))
            if origin.right:
                queue.append((origin.right, clone.right))



class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = None
        def find(o, c):
            nonlocal ans

            if o:
                find(o.left, c.left)
                if o == target:
                    ans = c
                find(o.right, c.right)

        find(original, cloned)
        return ans