import sys,math
n=int(sys.stdin.readline())
print(n//2+1)
x=[1,1]
for i in range(n):
    print(*x)
    x[i&1]+=1
