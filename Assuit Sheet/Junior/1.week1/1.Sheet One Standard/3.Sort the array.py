import sys,math
def solve():
    ans=[0]*(10**5+1)
    for i in arr:
        ans[i]+=1
    for i in range(10**5+1):
        if ans[i]:
           for j in range(ans[i]):
            print(i,end=" ")
n=int(sys.stdin.readline())
arr=list(map(int,map(int,sys.stdin.readline().split())))
solve()
