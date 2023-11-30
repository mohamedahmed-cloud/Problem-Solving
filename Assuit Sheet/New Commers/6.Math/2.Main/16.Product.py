def solve(L,R,M):
    ans=1
    for i in range(L,R+1):
        ans*=i
        ans=ans%M
    return ans


import sys,math
L,R,M=map(int,sys.stdin.readline().split())
print(solve(L,R,M))