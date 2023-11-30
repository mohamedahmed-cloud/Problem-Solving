import sys
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    print(a.index(i+1)+1,end=" ")
