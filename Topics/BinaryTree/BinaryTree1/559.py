# Definition for a Node.
class Node:
	def __init__(self, val=None, children=None):
		self.val = val
		self.children = children

class Solution:
	def maxDepth(self, root: 'Node') -> int:
		ans = 0
		curr = 1
		def dfs(node):
			nonlocal ans, curr

			if not node.children: return 1

			for i in node.children:
				curr += 1
				dfs(i)
				curr -= 1
			ans = max(ans, curr)
			return ans + 1
		return dfs(root)

node_14 = Node(14)
node_13 = Node(13)
node_12 = Node(12)
node_11 = Node(11)
node_10 = Node(10)
node_9 = Node(9)
node_8 = Node(8)
node_7 = Node(7)
node_6 = Node(6)
node_5 = Node(5, children=[node_12, node_13])
node_4 = Node(4, children=[node_10, node_11])
node_3 = Node(3, children=[node_8, node_9])
node_2 = Node(2, children=[node_6, node_7])
node_1 = Node(1, children=[node_2, node_3, node_4, node_5])

slv = Solution()
print(slv.maxDepth(node_1))
# The tree is now created.
