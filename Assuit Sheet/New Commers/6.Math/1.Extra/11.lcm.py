def lcm(a,b):
    return int(a*b/gcd(a,b))

def gcd(a,b):
    while b!=0:
        a1=a
        a=b
        b=a1%b
    return a
import sys,math
a,b = map(int, sys.stdin.readline().split())
print(lcm(a,b))