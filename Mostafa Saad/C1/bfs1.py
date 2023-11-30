#    Author : Mohamed Yousef 
#    Date   : 2023-05-07
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

# level for graph.

class Graph:
    def __init__ (self):
        self.Graph = defaultdict(list)
    def addEdges(self, u, v):
        self.Graph[u].append(v)
    def bfs(self, des, x, passM):
        queue = []
        visited = [False] * (passM + 1)
        print(f'max len: {(max(self.Graph) + 1)}')
        level = 0

        queue.append(des)
        visited[des] = True

        while queue:
            sz = len(queue)
            while sz:
                s = queue.pop(0)
                if x == s:
                    return level

                for i in self.Graph[s]:
                    print(f"curr i is: {i}")
                    if not visited[i]:
                        visited[i] = True
                        queue.append(i)
                sz -= 1
            level += 1
        return -1

# take input
v = test()
# edges = []
g = Graph()
first= "Yousef"
passM = - float('inf')
for _ in range( v  -1):
    u,v = (mvalues()) 
    if first == "Yousef":
        first = u
    passM = max(u, v, passM)
    g.addEdges(u, v)
x = test()
ans = g.bfs(first,x, passM)
print(ans )
# 5
# 0 1 
# 0 2 
# 1 3 
# 2 4
# 0