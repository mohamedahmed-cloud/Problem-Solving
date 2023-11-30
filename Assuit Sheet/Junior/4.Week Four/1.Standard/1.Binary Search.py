#    Author : Mohamed Yousef 
#    Date   : 2022-12-07
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n,q=map(int,sys.stdin.readline().split())
main=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    main.append((x,y))
ans=0
# ll=[]
for _ in range(q):
    w,x,y=map(str,sys.stdin.readline().split())
    x=(int(x),int(y))
    if w=="lower":
        ans=bisect.bisect_left(main,x)-1
    elif w=="upper":
        ans=bisect.bisect_right(main,x)
        if ans ==n:
            ans=-1
    elif w=="find":
        a=bisect.bisect_right(main,x)
        if a-1<n and main[a-1]==x:
            ans="found" 
        else:
            ans="not found"
    # ll.append(ans)
    print(ans)
# print(ll)