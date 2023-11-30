#    Author : Mohamed Yousef 
#    Date   : 2023-02-09
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
# A hard problem  😊
class Solution:
    def solve(self,ideas):
        l= [set() for _ in range(26)]
        ans=0
        for i in ideas:
            l[ord(i[0])-ord("a")].add(i[1:])
        for i in range(26):
            s1=l[i]
            x1=len(s1)
            for j in range(i,26):
                s2=l[j]
                x2=len(s2)
                s2=s2.union(s1)
                ans+=(len(s2)-x2)*(len(s2)-x1)
        return ans*2
        
solve=Solution()
print(solve.solve(["lack","back"]))
