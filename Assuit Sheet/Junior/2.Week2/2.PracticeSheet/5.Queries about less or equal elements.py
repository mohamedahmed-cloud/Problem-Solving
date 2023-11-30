import sys,math,bisect
n,m =map(int,sys.stdin.readline().split())
a=sorted(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
for i in b:
    print(bisect.bisect(a,i),end=' ')