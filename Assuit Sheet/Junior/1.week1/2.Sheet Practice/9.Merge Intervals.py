# Wrong answer on test two 
import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    l,r=map(int,sys.stdin.readline().split())
    l,r=min(l,r),max(l,r)
    hi=0
    for j in range(len(arr)):
        if (arr[j][0]>=l and arr[j][0]<=r) or (arr[j][1]>=l and arr[j][1]<=r) or (arr[j][0]<=l and arr[j][1]>=l) or (arr[j][0]<=r and arr[j][1]>=r):
            hi=1
            arr[j][0]=min(l,arr[j][0])
            arr[j][1]=max(r,arr[j][1])
            break
    if hi==0:
        arr.append([l,r]) 
for i in arr:
    print(*i)