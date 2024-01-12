#    Author : Mohamed Yousef 
#    Date   : 2024-01-11
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")
n, m = mvalues()
l1 = []
l2 = []
for i in range(n * 2):
    if i < n:
        l1.append(svalues())
    else:
        l2.append(svalues())

col1 = []
col2 = []
def cols(l, col):
    for i in range(m):
        save = set()
        for j in range(n):
            save.add(l[j][i])
        col.append(save)
cols(l1, col1)
cols(l2, col2)
# print(col1, col2)

def count(i):
    for j in col1[i]:
        if j in col2[i]:
            return 0
    return 1


ans = 0
for i in range(m):
    ans += count(i)
print(ans)



