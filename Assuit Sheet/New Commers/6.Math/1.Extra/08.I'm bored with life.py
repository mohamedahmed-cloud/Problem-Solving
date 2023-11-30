def solve(x,y):
    ans=1
    for i in range(1,min(x,y)+1):
        ans*=i
    return ans

import sys
x,y= map(int, sys.stdin.readline().split())
print(solve(x,y))