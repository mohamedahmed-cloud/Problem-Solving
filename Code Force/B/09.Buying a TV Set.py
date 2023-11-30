import sys,math
a,b,x,y=map(int,sys.stdin.readline().split())
g=math.gcd(x,y)
x//=g
y//=g
print(min(a//x,b//y))