import sys,math
n,m=map(int, sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.insert(0,0)
for i in range(m):
    j=int(sys.stdin.readline())
    sys.stdout.write(str(len(set(arr[j:])))+"\n")