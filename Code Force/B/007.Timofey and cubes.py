import sys,math
n=int(sys.stdin.readline())
l=list(map(int,sys.stdin.readline().split()))
for i in range(n//2):
    if i%2==0:
        l[i],l[n-i-1]=l[n-i-1],l[i]
print(*l)