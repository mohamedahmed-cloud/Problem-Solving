#    Author : Mohamed Yousef 
#    Date   : 2023-01-01
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(n):
    turn=0
    find=True
    while n>1:
        if n%2==0:
            x=n//2
            n-=x
            turn+=1
            find=True
        else:
            x=n//2
            find=False
            while x<0:
                if n%x==0:
                    n-=x
                    turn+=1
                    find=True
                    break
            if not find:
                n=0
        if turn%2!=0:
            return True
        else:return False

print(solve(3))

