import sys,math
def solve():
    arr=[0]*(n+1)
    for i in range(q):
        z,x=map(int,sys.stdin.readline().split())
        if z==1:
            arr[x]+=1
        if z==2:
            print(arr[x])
n,q=map(int,sys.stdin.readline().split())
solve()