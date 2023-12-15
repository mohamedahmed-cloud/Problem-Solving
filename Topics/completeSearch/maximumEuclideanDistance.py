#    Author : Mohamed Yousef 
#    Date   : 2023-12-14
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

n = test()
x = lvalues()
y = lvalues()
ans = -1
for i in range(n):
    for j in range(i + 1, n):
        dx = abs(x[i] - x[j])
        dy = abs(y[i] - y[j])
        tmp =  dx ** 2 + dy ** 2
        if tmp > ans: ans = tmp
print(ans)
