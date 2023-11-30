#    Author : Mohamed Yousef
#    Date   : 2023-05-01
import sys
import math
import bisect
import collections
import itertools
import heapq
from itertools import accumulate, combinations, permutations, chain
from collections import defaultdict, deque, Counter
sys.setrecursionlimit(50000)  # To increase Recursion depth in py
def mvalues(): return map(int, sys.stdin.readline().split())
def lvalues(): return list(map(int, sys.stdin.readline().split()))
def svalues(): return sys.stdin.readline().strip()
def test(): return int(sys.stdin.readline())


n, m, k = mvalues()
arr = lvalues()
operation = [0] * (m + 1)
store = []

for i in range(m):
    store.append(lvalues())
# print(store)

for i in range(k):
    a, b = mvalues()
    operation[a - 1] += 1
    operation[b] -= 1

for i in range(1, m):
    operation[i] += operation[i - 1]
# print(operation)

ans = [0] * (n + 1)
for i in range(m):
    ans[store[i][0] - 1] += (operation[i] * store[i][2])
    ans[store[i][1]] -= (operation[i] * store[i][2])
# print(ans)
for i in range(1, n):
    ans[i] += ans[i - 1]

for i in range(n):
    ans[i] += arr[i]

# print(ans)
ans = ans[:-1]
sys.stdout.write(" ".join(map(str, ans)))
