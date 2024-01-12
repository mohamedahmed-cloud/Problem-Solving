#    Author : Mohamed Yousef 
#    Date   : 2024-01-07
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
    x = y = float("inf")
    ans = 0
    # I need to keep track of one have highest value that's can and another have another value
    for i in range(n):
        # y have the make value of x
        if x > y: x, y = y, x

        if x >= l[i]:
            x = l[i]
        elif y >= l[i]:
            y = l[i]
        else:
            x = l[i]
            ans += 1

    print(ans)

