#    Author : Mohamed Yousef 
#    Date   : 2023-02-15
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
class Solution:
    def solve(self,num,k):
        return [int(x) for x in  list(str(int("".join(map(str,num)))+(k)))]
        



solve=Solution()
print(solve.solve([1,2,0,0],34))