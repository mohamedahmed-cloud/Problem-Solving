def fib(n):
    if n==1 or n==0:
        return n
    return fib(n-1)+fib(n-2)


import sys
n=int(sys.stdin.readline())
print(fib(n))