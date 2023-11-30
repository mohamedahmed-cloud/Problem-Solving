#    Author : Mohamed Yousef 
#    Date   : 2022-12-02
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n=int(sys.stdin.readline())
if n==1 or n==2 : 
    print("No")

else:
    print("Yes")
    x=math.ceil(n/2)
    print(1,x)
    print(n-1,end=' ')
    for i in range(1,n+1):
        if i!=x:
            print(i,end=' ')
