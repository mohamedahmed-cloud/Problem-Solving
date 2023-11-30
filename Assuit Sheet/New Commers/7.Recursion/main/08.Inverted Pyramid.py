def Pyramid(arr,n,a):
    if n==0:
        for i in range(len(arr)-1,-1,-1):
            print(arr[i])
        return 0
    if a==1:
        arr.append((n-1)*" "+"*"*1)
    else:       
        arr.append((n-1)*" "+"*"*(a))
    return Pyramid(arr,n-1,a+2)

import sys,math
n=int(sys.stdin.readline())
a=1
arr=[]
Pyramid(arr,n,a)