#!/usr/bin/env python3
from collections import defaultdict
class DFS:
	def __init__(self):
		self.graph = defaultdict(list)

	def add(self, u, v):
		self.graph[u].append(v)

	def make_dfs(self, start, visited):
		visited.add(start)
		print(start)
		for node in self.graph[start]:
			if node not in visited:
				self.make_dfs(node, visited)
	def prepare_dfs(self, start):
		visited = set()
		self.make_dfs(start, visited)



dfs = DFS()
dfs.add(0, 1)
dfs.add(0, 2)
dfs.add(1, 2)
dfs.add(2, 0)
dfs.add(2, 3)
dfs.add(3, 3)
dfs.prepare_dfs(2)
