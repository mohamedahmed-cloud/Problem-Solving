# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		needed = []
		def divide(arr):
			if len(arr) <= 1:
				return None
			mid = len(arr) // 2
			L = arr[:mid]
			R = arr[mid:]
			needed.append(arr[mid])
			divide(L)
			divide(R)

		def createBST(node, value):
			if not node:
				return TreeNode(value)
			temp = node
			while  True:
				if node.val > value:
					if not node.left:
						node.left = TreeNode(value)
						return temp
					node = node.left

				elif node.val < value:
					if not node.right:
						node.right = TreeNode(value)
						return temp
					node = node.right
			
		divide(nums)
		needed = needed + [nums[0]]
		node = None
		for i in needed:
			node = createBST(node, i)
		
		return node

slv = Solution()
nums = [1,2,3,4]
node = slv.sortedArrayToBST(nums)
def print_node(node):
	def dfs(node):
		if node:
			print(node.val)
			dfs(node.right)
			dfs(node.left)
	dfs(node)
print_node(node)
