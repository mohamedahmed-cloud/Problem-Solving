#!/usr/bin/env python3

class Graph:
	def __init__(self, vertices):
		self.v = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

	def minDistance(self, dist, sep_set):
		min = float("inf")
		for u in range(self.v):
			if dist[u] < min and sep_set[u] == False:
				min = dist[u]
				min_index = u

		return min_index


	def dijkstra(self, src):
		dist = [float("inf")] * self.v
		dist[src] = 0
		spt_set = [False] * self.v
		for count in range(self.v):
			x = self.minDistance(dist, spt_set)
			spt_set[x]  = True
			for i in range(self.v):
				if self.graph[x][i] > 0 and spt_set[i] == False and \
				dist[i] > dist[x] + self.graph[x][i]:
					dist[i] = dist[x] + self.graph[x][i]

