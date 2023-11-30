def solve(arr):
    arr.insert(0,0)
    for i in range(1,n+1):
        arr[i]+=arr[i-1]


import sys,math
n,q=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
solve(arr)
# print(arr)
for i in range(q):
    l,r=map(int,sys.stdin.readline().split())
    print(arr[r]-arr[l-1])