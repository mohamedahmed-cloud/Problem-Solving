#    Author : Mohamed Yousef 
#    Date   : 2023-06-27
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    n = test()
    l = lvalues()
    flag = True

    pos = [[] for i in range(n + 1)]

    for i,value in enumerate(l):
        pos[value].append(i)

    p,q = [0] * n, [0] * n
    pr, pq = [], []
    # print(pos)

    for i in range(n, 0, -1):
        if len(pos[i]) == 2:
            p[pos[i][0]] = l[pos[i][0]]
            q[pos[i][1]] = l[pos[i][1]]
            pr.append(pos[i][1]) 
            pq.append(pos[i][0])
            continue

        if len(pos[i]) == 1:
            p[pos[i][0]] = l[pos[i][0]] 
            q[pos[i][0]] = l[pos[i][0]]
            continue

        if pr and pq:
            p[pr.pop()] = i
            q[pq.pop()] = i

        else:
            flag = False

    if flag:
        print("YES")
        print(*q)
        print(*p)

    else:
        print("NO")


