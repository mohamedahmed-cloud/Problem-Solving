def PrintNumber(store,n):
    if n==0:
        return n
    print(store-n+1)
    return PrintNumber(store,n-1)

import sys,math
n=int(sys.stdin.readline())
ans=[]
store=n
PrintNumber(store,n)