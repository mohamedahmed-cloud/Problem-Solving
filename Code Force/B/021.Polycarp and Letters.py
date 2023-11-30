#    Author : Mohamed Yousef 
#    Date   : 2022-12-06
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
n=int(sys.stdin.readline())
s=sys.stdin.readline().strip()
newsring=s[0]
if n>2:
    for i in range(1,n):
        if s[i-1]!=s[i]:
            newsring+=s[i]
    s=newsring
else:
    s=set(s)
out=0
ans=0
# print(s)
myset=set()
for i in s:
    if i.lower() == i :
        if i not in myset:
            myset.add(i)
            out+=1
    else:
        myset=set()
        out=0
    ans=max(ans,out)
print(ans)