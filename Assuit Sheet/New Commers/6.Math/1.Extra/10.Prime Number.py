# Time limit in test 5 
def solve(arr,b):
    summations=0
    mul=1
    mul=b**sum(arr)
    for i in arr:
        summations+=int(mul/(b**i))
    # print(summations,mul)
    ans=gcd(summations,mul)
    ans=ans%((10e8)+7)
    return int(ans)
def gcd(summations,mul):
    while mul!=0:
        a=summations
        summations=mul
        mul=a%summations
    return summations

import sys,math
a,b= map(int, sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
print(solve(arr,b))