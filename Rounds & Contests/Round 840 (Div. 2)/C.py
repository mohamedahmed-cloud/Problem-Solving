#    Author : Mohamed Yousef 
#    Date   : 2023-06-22
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())
t = test()

for _ in range(t):
    n = test()
    l = lvalues()
    if n == 1:
        print(*l)
    elif n == 2:
        print(max(sum(l), abs(l[0] - l[1]) * 2))
    elif n == 3:
        x = []
        x.append(sum(l))
        x.append(3 * l[0])
        x.append(3 * l[2])
        x.append(2 * abs(l[0] - l[1]) + l[2])
        x.append(2 * abs(l[0] - l[1]) + abs( abs(l[0] - l[1]) - l[2]))
        x.append(2 * abs(l[1] - l[2]) + l[0])
        x.append(2 * abs(l[1] - l[2]) + abs( abs(l[1] - l[2]) - l[0]))
        x.append(3 * abs(l[0] - l[1]))
        x.append(3 * abs(l[1] - l[2]))
        # print(x)
        print(max(x))
    elif n >= 4:
        print(n * max(l))
