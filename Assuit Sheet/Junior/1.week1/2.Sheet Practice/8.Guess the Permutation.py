# can't understand the problem it self 
import sys,math
n=int(sys.stdin.readline())
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
print(n,end=' ')
for i in range(n-1,0,-1):
    print(i,end=' ')
print()