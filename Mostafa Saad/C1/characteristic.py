#    Author : Mohamed Yousef 
#    Date   : 2023-05-07
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

t = test()
for _ in range(t):
    n, c = mvalues()

    ans = [1] * n
    currN = n
    currC = (currN + 1) * currN //2
    i = 0

    while currC != c and i < n:
        currN -= 1
        ans[i] = -1
        i += 1

        currC = (currN - 1) * currN // 2 
        if i > 1:
            currC += (i - 1) * i // 2

    if currC == c:
        print("YES")
        print(*ans)
    else:
        print("NO")