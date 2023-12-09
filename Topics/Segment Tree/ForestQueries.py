#    Author : Mohamed Yousef 
#    Date   : 2023-12-05
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(str,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

n, m = mvalues()
matrix = []
for i in range(n):
    matrix.append(list(svalues()))
# operation
# print(matrix)
prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        curr = 0
        if  matrix[i - 1][j - 1] == "*":
            curr = 1
        prefix[i][j] = prefix[i ][j - 1] + curr
        # prefix[j][i] = prefix[j][i - 1] + curr


for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] += prefix[i - 1][j]


for i in range(m):
    x1, y1, x2, y2 = mvalues()
    ans = prefix[x2][y2] - prefix[x1 -1][y2] - prefix[x2][y1 -1] + prefix[x1 - 1][y1 -1]
    print(f"{ans} ")
