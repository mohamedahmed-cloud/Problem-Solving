import sys,math
def solve():
    arr=[]
    for i in range(n):
        l,r=map(int, sys.stdin.readline().split())
        if l==1:
            arr.append(r)
        elif l==2:
            if arr[0]==r:
                print("Yes")
            else:print("No")
            arr=arr[1:]
n=int(sys.stdin.readline())
solve()