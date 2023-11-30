import sys,math
def solve(out):
    s=0
    for i in range(1,len(arr)):
        s+=int(arr[i])
    arr.insert(1,s)
    out.append(arr)
n=int(sys.stdin.readline())
out=[]
for i in range(n):
    arr=list(map(str,sys.stdin.readline().split()))
    solve(out)
out.sort()
ans=sorted(out,key=lambda x:x[1],reverse=True)
for i in ans:
    print(*i)
