import sys,math
n=int(sys.stdin.readline())
a=[]
for i in range(n):
    a.append(input())
# a=list(map(int, sys.stdin.readline().split()))
count=1
for i in range(1,n):
    if a[i-1]!=a[i]:
        count+=1
print(count)