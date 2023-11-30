def solve(n,p):
    out=1
    ans=1
    for i in range(n-p+1,n+1):
        out*=i
    for i in range(2,p+1):
        ans*=i
    return (out,out//ans)
import sys
n,p=map(int,sys.stdin.readline().split())
ans=solve(n,p)
print(ans[1],end=" ")
print(ans[0])