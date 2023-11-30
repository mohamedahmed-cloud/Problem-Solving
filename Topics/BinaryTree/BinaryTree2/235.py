# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		p = p.val
		q = q.val

		def dfs(root):
			if root:
				if root.val < p and root.val < q:
					return dfs(root.left)
				elif root.val > p and root.val > q:
					return dfs(root.right)
				else:
					return root

		return dfs(root)
			