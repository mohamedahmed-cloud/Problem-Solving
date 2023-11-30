def solve(n,ans):
    if n==0:
        return ans
    ans*=n
    return solve(n-1,ans)

import sys,math
ans=1
n=int(sys.stdin.readline())
print(solve(n,ans))