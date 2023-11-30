def Max_Number(n,arr,ans):
    if n==0:
        return ans
    if ans<arr[n-1]:
        ans=arr[n-1]
    return Max_Number(n-1,arr,ans)
import sys,math
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
ans=arr[0]
print(Max_Number(n,arr,ans))