#    Author : Mohamed Yousef 
#    Date   : 2023-06-26
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
    ans = []
    if n == 3:
        print("NO")
        continue
    if n % 2 == 0:
        print("YES")
        for i in range(n):
            ans.append(-1 if i % 2 else 1)
        print(*ans)
    else:
        print("YES")
        for i in range(n):
            ans.append(-(n//2) if i % 2 else n//2 -1)
        # for i in range(1,n):
            # print(ans[i] + ans[i - 1],end= " ")
        # print(sum(ans))
        print(*ans)


