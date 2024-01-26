#    Author : Mohamed Yousef 
#    Date   : 2024-01-23
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(str,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

sys.stdin = open("guess.in", "r")
sys.stdout = open("guess.out", "w")
features = []
n = test()
for _ in range(n):
    l = lvalues()
    bird = l[0]
    features.append(set(l[2:]))

ans = 0
# print(features)
for i in range(n):
    for j in range(i + 1, n):
        # print(features[i], features[j])
        # print(features[i].intersection(features[j]))
        curr = len(features[i].intersection(features[j]))
        if curr > ans:
            ans = curr
print(ans + 1)

