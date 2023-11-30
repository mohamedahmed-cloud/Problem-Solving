def gcd(a,b):
    iter=0
    while b:
        iter+=a//b
        a,b=b,a%b
    return iter

import sys
a,b=map(int, sys.stdin.readline().split())
print(gcd(a,b))