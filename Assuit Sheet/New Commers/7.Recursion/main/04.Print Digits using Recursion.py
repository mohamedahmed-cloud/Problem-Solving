def solve(store,s,n):
    if n==0:
        return 0
    if n==1:
        print(s[store-n])
    else:
        print(s[store-n],end=" ")
    solve(store,s,n-1)

import sys,math
t=int(sys.stdin.readline())
for i in range(t):
    s=sys.stdin.readline()
    s=s[:-1]
    n=len(s)
    store=n
    solve(store,s,n)
