#    Author : Mohamed Yousef 
#    Date   : 2023-12-28
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    V = "ae"
    C = "bcd"
    # CV or CVC
    n = test()
    s = svalues()
    ans = []
    i = 0
    while i < n - 1:
        if s[i] in C and s[i + 1] in C :
            ans.pop()
            ans.append(s[i])
            ans.append(".")
            
        elif s[i] in V and s[i + 1] in C:
            ans.append(s[i])
            ans.append(".")
        else:
            ans.append(s[i])
        i += 1
    if ans[-1] == ".": ans.pop()
    ans.append(s[-1])
    ans = "".join(ans)
    print(ans)




