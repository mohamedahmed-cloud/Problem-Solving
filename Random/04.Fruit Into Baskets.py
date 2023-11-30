#    Author : Mohamed Yousef 
#    Date   : 2023-02-07
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,fruits):
        dict1=defaultdict(int)
        j=i=0
        for i,value in enumerate(fruits):
            dict1[value]+=1
            if len(dict1)>2:
                dict1[fruits[j]]-=1
                if not dict1[fruits[j]]:
                    dict1.pop(fruits[j])
                j+=1
        return i-j+1
            
solve=Solution()
print(solve.solve([1,0,1,4,1,4,1,2,3]))