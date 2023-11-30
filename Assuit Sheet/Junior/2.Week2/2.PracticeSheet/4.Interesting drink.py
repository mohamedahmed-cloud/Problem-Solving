import sys,math,bisect
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr=sorted(arr)
q=int(sys.stdin.readline())
left=0
right=n-1
for i in range(q):
    key=int(sys.stdin.readline())
    print(bisect.bisect(arr,key))
    