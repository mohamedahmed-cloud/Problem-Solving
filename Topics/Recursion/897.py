# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l = []
        saveRoot = root
        def convertToSkewed(root):
            if root.right:
                convertToSkewed(root.right)

            l.append(root.val)

            if root.left:
                convertToSkewed(root.left)
            
        convertToSkewed(root)
        l.sort()
        root = saveRoot

        dummy = TreeNode(0)
        curr = dummy
        
        for i in l:
            curr.right = TreeNode(i)
            curr = curr.right
            
        return dummy.right
    
# another solution

# Definition for a binary tree node.
# optimal solution 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        head = prev = None

        def convert(root):
            if not root:
                return
            
            convert(root.left)

            nonlocal head, prev
            
            if not head:
                head = root
                head.left = None
                prev = root
            else:
                prev.right = root
                root.left = None
                prev = root
            convert(root.right)
            
        convert(root)
        return head 
