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

s, m = 0, 0
ans = []

n, k = mvalues()
arr = lvalues()
m1 = max(arr)
m2 = min(arr)
k1 = k
while k > 0 and (m1 - m2 > 1 ):
    k -= 1
    i = arr.index(m1)
    j = arr.index(m2)
    ans.append([i + 1, j + 1])
    arr[i] -= 1
    arr[j] += 1
    m1 = max(arr)
    m2 = min(arr)
    # print(ans)
    
print(max(arr) - min(arr), k1 - k)
for i in ans:
    print(*i)