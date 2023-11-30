import sys,math
def solve(ans):
    l,r,val=map(int,sys.stdin.readline().split())
    ans[l]+=val
    if r<n:
        ans[r+1]-=val
n,q=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
# arr.insert(0,0)
ans=[0]*(n+1)
for i in range(q):
    solve(ans)
for i in range(1,n+1):
    ans[i]+=ans[i-1]
ans=ans[1:]
# arr=arr[1:]
for i in range(n):
    arr[i]+=ans[i]
    print(arr[i],end=" ")
