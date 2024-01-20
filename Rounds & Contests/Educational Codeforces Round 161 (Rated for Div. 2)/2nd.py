#    Author : Mohamed Yousef 
#    Date   : 2024-01-18
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    n = test()
    l = lvalues()
    l.sort()
    cnt = Counter(l)
    if n < 3: print(0); continue
    # cnt = sorted(cnt.items())
    # print(cnt)
    ans = 0
    prev = 0
    for key, val in cnt.items():
        if val > 2:
            ans += (val) * (val - 1) * (val - 2) // 6
        if prev > 0:
            ans += prev * (val * (val - 1)) // 2
        prev += val
    print(ans)

