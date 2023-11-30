def solve(n,arr,ans):
    if n==0:
        return ans
    ans+=arr[n-1]
    return solve(n-1,arr,ans)

import sys,math
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
ans=0
print(solve(n,arr,ans))