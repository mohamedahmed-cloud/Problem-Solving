#    Author : Mohamed Yousef 
#    Date   : 2023-02-12
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,n,redEdges,blueEdges):
        red=defaultdict(list)
        blue=defaultdict(list)
        answer=[-1 for x in range(n)]
        for key,value in redEdges:
            red[key].append(value)
        for key,value in blueEdges:
            blue[key].append(value)
        queue=deque()
        queue.append([0,0,None])
        visited=set()
        visited.add((0,None))
        while queue:
            node,lenght,color=queue.popleft()
            if answer[node]==-1:
                answer[node]=lenght
            if color !="RED":
                for n in red[node]:
                    if (n,"RED") not in visited:
                        visited.add((n,"RED"))
                        queue.append([n,lenght+1,"RED"])
            if color !="BLUE":
                for n in blue[node]:
                    if (n,"BLUE") not in visited:
                        visited.add((n,"BLUE"))
                        queue.append([n,lenght+1,"BLUE"])
        return answer


solve=Solution()
print(solve.solve(3,[[0,1],[1,2]],[]))
