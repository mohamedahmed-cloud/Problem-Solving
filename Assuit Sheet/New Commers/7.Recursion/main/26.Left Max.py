# Runtime error because make recursion alot of times
def solve(n,arr,st):
    if st==n:
        return arr
    arr[st]=max(arr[st],arr[st-1])
    return solve(n,arr,st+1)

import sys,math
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
st=1
# print(*solve(n,arr,st))
for i in range(1,n):
    arr[i]=max(arr[i],arr[i-1])
print(*arr)
