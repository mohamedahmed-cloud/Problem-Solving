#    Author : Mohamed Yousef 
#    Date   : 2023-12-18
import sys,math,bisect,collections,itertools,heapq
from itertools  import accumulate ,combinations ,permutations,chain
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()
def test():return int(sys.stdin.readline())

for _ in range(test()):
    dict = defaultdict(int)
    s = svalues()
    n = len(s)

    for val in s:
        dict[val] += 1
    # print(dict)
    ans = 0
    for i in range(n):
        if s[i] == "0" and dict["1"] > 0:
            dict["1"] -= 1
        elif s[i] == "1" and dict["0"] > 0:
            dict["0"] -= 1
        else:
            ans = (n - i)
            break
    print(ans)
    