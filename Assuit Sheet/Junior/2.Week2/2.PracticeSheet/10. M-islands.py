import sys,math,bisect
n,m=map(int, sys.stdin.readline().split())
arr=[0]*(m+1)
for i in range(n):
    a,b=map(int, sys.stdin.readline().split())
    for j in range(a,b+1):
        arr[j]+=1
q=int(sys.stdin.readline())
for j in range(q):
    c,d=map(int, sys.stdin.readline().split())
    if arr[c]!=0 and arr[d]!=0:
        print("YES")
    else:print("NO")
print(arr)