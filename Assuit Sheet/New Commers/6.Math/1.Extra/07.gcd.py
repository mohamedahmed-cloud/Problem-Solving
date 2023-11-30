from time import time
def gcd(x,y):
    a,b=1,1
    while a!=0 and b!=0:
        a=max(x,y)
        b=min(x,y)
        a=a-b
        x=a
        y=b
    return max(a,b)
# another one 
def gcd2(a,b):
    while b!=0:
        a2=a
        a=b
        b=a2%b
    return a

import sys,math
n,y=map(int, sys.stdin.readline().split())
start=time()
print(gcd2(n,y))
end=time()
print(end-start)

start=time()
print(gcd(n,y))
end=time()
print(end-start)

start=time()
print(math.gcd(n,y))
end=time()
print(end-start)