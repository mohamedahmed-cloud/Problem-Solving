from collections import defaultdict
class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
        # print(self.graph)
    def bfs(self, des):
        queue = []
        visited = [False] * (len(self.graph) + 1)

        queue.append(des)
        visited[des] = True
        

        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
        


g = Graph()
try:
    while True:
        u, v = map(int,input().split())
        g.addEdge(u, v)
except:
    pass
        
g.bfs(2)
print()
# 0 1
# 0 2 
# 1 2 
# 2 0 
# 2 3 
# 3 3 