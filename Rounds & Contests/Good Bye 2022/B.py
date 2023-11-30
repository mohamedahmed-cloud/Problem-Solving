#    Author : Mohamed Yousef 
#    Date   : 2023-06-25
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    n, k = mvalues()
    cnt = 1
    big = n
    ans = []
    for i in range(n):
        if i % 2 == 0:
            ans.append(big)
            big -= 1
        else:
            ans.append(cnt)
            cnt += 1
    print(*ans)