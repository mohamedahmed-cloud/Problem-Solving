def Pyramid(n,a):
    if n==0:
        return 0
    if a==1:
        print((n-1)*" "+"*"*1)
    else:       
        print((n-1)*" "+"*"*(a))
    return Pyramid(n-1,a+2)

import sys,math
n=int(sys.stdin.readline())
a=1
Pyramid(n,a)