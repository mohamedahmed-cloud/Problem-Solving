import sys,math,bisect,itertools
n,k=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
l.sort()
if k>0:
    k-=1
else:
    x=l[0]
    x-=1
    x=x if x>0 else -1
    print(x)
    quit()
a=l[k]
if k<n-1:
    if a==l[k+1]:
        print(-1)
    else:print(a)
else:
    print(l[k])