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


all = []
try:
    while True:
        xnumber = lvalues()
        xnumber.reverse()
        if not xnumber:
            break
        xvalues = lvalues()
        ans = []
        for i  in xvalues:
            iter = 0
            function = 0
            for j in xnumber:
                function += j * i ** iter
                iter += 1
            ans.append(function)
        all.append(ans)
except:
    pass
for i in all:
    print(*i)