#    Author : Mohamed Yousef 
#    Date   : 2023-12-23
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

n, m = mvalues()
count = defaultdict(list)
for i in range(n):
    l = lvalues()
    for i in range(m):
        count[l[i]].append(i)

indxes = list(count.values())
ans = 0
def compare(arr1, arr2):
    tmp = 0
    for i, j in zip(arr1, arr2):
        if i > j:
            tmp += 1
        else:
            tmp -= 1
    return abs(tmp) == len(arr1)


for i in range(m):
    for j in range(i + 1, m):
        ans += compare(indxes[i], indxes[j])
        # break
print(ans)