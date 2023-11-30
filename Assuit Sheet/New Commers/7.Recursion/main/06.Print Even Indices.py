def PrintEven(n,arr):
    if n<0:
        return
    if n%2==0:
        if n==0:
            print(arr[n],end="")
        else:
            print(arr[n],end=" ")
    return PrintEven(n-1,arr) 

import sys,math
n=int(sys.stdin.readline())-1
arr=list(map(int,sys.stdin.readline().split()))
PrintEven(n,arr)
