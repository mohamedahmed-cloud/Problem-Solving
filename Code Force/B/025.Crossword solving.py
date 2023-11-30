#    Author : Mohamed Yousef 
#    Date   : 2023-02-04
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque,Counter
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def mvalues():return map(int,sys.stdin.readline().split())
def lvalues():return list(map(int,sys.stdin.readline().split()))
def svalues():return sys.stdin.readline().strip()

n,m=mvalues()
s=svalues()
t=svalues()
cnt=0
location=[]
res=10e5
for i in range(n,m+1):
    s1=t[cnt:i]
    cnt+=1
    def find(s1,s):
        ans=0
        loc=set()
        for i in range(n):
            if s1[i]==s[i]:
                ans+=1
            else:
                loc.add(i+1)
        return ans,loc
    l=find(s1,s)
    # print(s1,s)
    ans=n-l[0]
    if ans<res:
        res=ans
        location=l[1]

print(res)
print(*list(location))



