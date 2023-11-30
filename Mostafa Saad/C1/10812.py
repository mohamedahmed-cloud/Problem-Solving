#    Author : Mohamed Yousef 
#    Date   : 2023-05-05
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

t = test()
ans = []
while (t):
    t -= 1
    s, d = mvalues()
    a1 = (s + d ) // 2
    a2 = (s + d ) / 2
    if a1 != a2:
        ans.append(["impossible"])
    elif s >= d:
        ans.append(sorted([(s + d ) // 2, (s - (s + d ) // 2)], reverse=True))
    else:
        ans.append(["impossible"])

for i in ans:
    print(*i)