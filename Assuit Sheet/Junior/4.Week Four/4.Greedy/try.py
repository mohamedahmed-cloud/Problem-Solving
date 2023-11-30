#    Author : Mohamed Yousef 
#    Date   : 2022-12-31
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(list,m):
    freq=[0]*(m+1)
    ans=-1
    store=0
    for i in list:
        freq[i]+=1
    for i,value in enumerate(freq):
        if i >ans:
            ans=i
            store=value
    return ans,value
# print(solve( [5,2,5,2,5,5],5))

# ---------------------
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(15,255))
print(gcd(15,255))


# ----------------------------------------------------------------
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
n=int(input())
ans=0
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        if i*i==n:
            ans+=1
        else:
            ans+=2

print(ans)
