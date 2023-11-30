def Sum_odd(n):
    oddterms=(n+1)//2
    return oddterms**2

def Sum_Even(n):
    Eventerms=(n)//2
    return Eventerms*(Eventerms+1)
def solve(a,b):
    l=min(a,b)
    h=max(a,b)
    odd=int(Sum_odd(h)-Sum_odd(l-1))
    even=int(Sum_Even(h)-Sum_Even(l-1))
    return (odd+even),even,odd
import sys,math
a,b=map(int,sys.stdin.readline().split())
ans=solve(a,b)
print(ans[0])
print(ans[1])
print(ans[2])
