#    Author : Mohamed Yousef 
#    Date   : 2022-12-25
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py

t=int(sys.stdin.readline())
for _ in range(t):
    n=int(sys.stdin.readline())
    l=[0]*10
    x=list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        l[x[i]%10]+=1
    # print(l)
    boolean=False
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i==j and j==k and l[i]<3:
                    continue
                if i==j and l[i]<2:
                    continue
                if i==k and l[i]<2:
                    continue
                if j==k and l[j]<2:
                    continue
                if(i+j+k)%10==3 and l[i]!=0 and l[j]!=0 and l[k]!=0:
                    # print(i,j,k)
                    print("YES")
                    boolean=True
                    break
            if boolean:
                break
        if boolean:
            break
    if not boolean:
        print("NO")


