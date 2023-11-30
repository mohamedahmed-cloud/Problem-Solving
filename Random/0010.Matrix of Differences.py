#    Author : Mohamed Yousef 
#    Date   : 2023-01-08
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
for _ in range(int(input())):
    n=int(input())
    x=1
    y=n*n
    l= [[0 for x in range(n)] for y in range(n)] 
    for i in range(n):
        if(i%2==0):
            for j in range(n):
                if(j%2==0):
                    l[i][j]=x
                    x+=1
                else:
                    l[i][j]=y
                    y-=1
        else:
            for j in range(n-1,-1,-1):
                if(j%2==0):
                    l[i][j]=y
                    y-=1
                else:
                    l[i][j]=x
                    x+=1
    for i in l:
        print(*i)
