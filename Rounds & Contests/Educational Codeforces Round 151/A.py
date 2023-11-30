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
    n, k, x = mvalues()

    if x != 1:
        print("YES")
        print(n)
        print(*([1] * n))

    else:
        if k == 1:
            print("NO")
            
        elif k == 2:
            if n % 2:
                print("NO")
            else:
                print("YES")
                print(n // 2)
                print(*([2] * (n //2)))
        else:
            print("YES")
            if n % 2 == 0:
                print(n // 2)
                print(*([2] * (n //2)))
            else:
                print(n // 2)
                print(*([2] * (n //2 - 1)+ [3]))

