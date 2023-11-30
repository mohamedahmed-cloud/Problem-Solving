def factorial(a,ans):
    if a>0:
        if a==0:
            return ans
        ans*=a
        return factorial(a-1,ans)
    else:
        if a==0:
            return ans
        ans*=a
        return factorial(a+1,ans)
def solve(n,r,final):
    ans=1
    b=factorial(n,ans)
    c=factorial(r,ans)
    d=factorial(n-r,ans)
    final=b/(c*d)
    return final

import sys,math
n,r= map(int, sys.stdin.readline().split())
# if n>=r:
final=0
print(int(solve(n,r,final)))
# else:print()
