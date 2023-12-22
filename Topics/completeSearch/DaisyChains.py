#    Author : Mohamed Yousef 
#    Date   : 2023-12-21
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

n = test()
arr = lvalues()
ans = 0
for i in range(n):
    save = defaultdict(int)
    count = 0
    cnt = 0
    for j in range(i, n):
        count += arr[j]
        cnt += 1
        save[arr[j]] = 1
        tmp = count / cnt
        if int(tmp) == tmp:
            # print(save, tmp, count, cnt)
            if save[tmp] != 0:
                ans += 1
print(ans)
