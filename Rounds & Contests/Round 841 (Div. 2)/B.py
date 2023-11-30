#    Author : Mohamed Yousef 
#    Date   : 2023-06-23
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())


mod = 10**9 + 7
t = test()

for _ in range(t):
    n = test()

    xsquaremulTwo = n * (n+1) * (2 * n+1) // 3
    sumFromOneTON = n * (n + 1) // 2
    ans = (xsquaremulTwo - sumFromOneTON ) 
    ans = ans * 2022 % mod

    print(ans)