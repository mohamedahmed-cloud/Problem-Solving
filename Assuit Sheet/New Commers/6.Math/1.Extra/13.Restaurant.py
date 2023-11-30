# From Hackerrank
import sys,math
t=int(sys.stdin.readline())
for i in range(t):
    n,p=map(int,sys.stdin.readline().split())
    if n==p:print(1)
    else:
        x=math.gcd(n,p)
        ans=(n/x)*(p/x)
        print(int(ans))