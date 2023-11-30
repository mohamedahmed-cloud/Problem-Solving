#    Author : Mohamed Yousef 
#    Date   : 2023-07-03
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    passWord = svalues()
    m = test()
    l = svalues()
    r = svalues()
    trunc = 0
    temp = 0
    def slv():
        # print(trunc,m)
        global m,l,r,trunc,temp
        for i in range(m):
            # temp = 0
            # print(temp, trunc)
            for j in range(int(l[i]), int(r[i]) + 1):
                if str(j) not in passWord[trunc:]:return "YES"
                else: temp = max(temp, trunc + passWord[trunc:].index(str(j)))
            trunc = temp + 1
        return "NO"
    print(slv())


    