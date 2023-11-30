def solve(n,m,ans):
    ans+=1
    if m==n:
        return 1
    if m<n:
        return 0
    return solve(n+1,m,ans)+solve(n+2,m,ans)+solve(n+3,m,ans)


import sys,math
n,m=map(int,sys.stdin.readline().split())
ans=0
print(solve(n,m,ans))
