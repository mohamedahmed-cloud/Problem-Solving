def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
import sys,math
n=int(sys.stdin.readline())
print(fib(n-1))