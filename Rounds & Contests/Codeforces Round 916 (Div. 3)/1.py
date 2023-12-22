#    Author : Mohamed Yousef 
#    Date   : 2023-12-19
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
prepare = []
for i in range(1, 27):
    prepare.append(i)

for _ in range(test()):
    n = test()
    s = svalues()
    ans = 0
    dict = defaultdict(int)
    for i in s:
        dict[i] += 1
    for key, val in dict.items():
        if val >= prepare[ord(key) - ord("A")]:
            ans += 1
    print(ans)

    