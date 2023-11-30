# Make run time error because recursion is 10e5

def solve(n,arr,ans):
    if n==0:
        return ans
    ans+=arr[n-1]
    return solve(n-1,arr,ans)
import sys
n,m=map(int,sys.stdin.readline().split())
arr =list(map(int,sys.stdin.readline().split()))
ans=0
arr=arr[n-m:]
n=m
# print(solve(n,arr,ans))
for i in arr:
    ans+=i
print(ans)
