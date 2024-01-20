#    Author : Mohamed Yousef 
#    Date   : 2024-01-13
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
final = []
for _ in range(test()):
    n, k, x = mvalues()
    l = lvalues()
    l.sort()
    for i in range(1, x + 1):
        l[-i] *= -1
    summation = sum(l)
    prev = summation
    profit = True
    currK = -1
    currX = -(x)
    # print(l)
    while k > 0:
        l[currK] *= -1
        summation += l[currK]


        currK -= 1
        k -= 1
        if abs(currX) < n:
            currX -= 1
            l[currX] *= -1
            summation += (l[currX]) * 2


        # print("prev", prev,"summation ", summation, l, n)
        if summation >= prev: 
            prev = summation
            
        # else:
        #     profit = False

    # print(sum(l[:currK]))
    final.append(max(prev, summation))
print(*final)