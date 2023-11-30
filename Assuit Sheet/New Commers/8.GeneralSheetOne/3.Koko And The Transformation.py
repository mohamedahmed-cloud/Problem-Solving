import sys
n,m=map(int,sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
if sum(a)==sum(b):
    print("Yes")
else:print("No")