from time import time
# import functools
# @functools.lru_cache(None)
# def fib_lru(n):
#     if n==0 or n==1:
#         return n
#     return fib_lru(n-1) + fib_lru(n-2)
import math

def Fibonacci(n):
   Q1=(1+math.sqrt(5))/2
   Q2=(1-math.sqrt(5))/2
   return round((math.pow(Q1,n)+math.pow(Q2,n))/math.sqrt(5))
    # print(n3)
    # return n3
n=int(input())
start=time()
print(Fibonacci(n))
end=time()
print(end-start)

def Fibonaci(n):
    n1=1
    n2=1
    n3=1
    for i in range(2,n):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n3)
    return n3
start=time()
Fibonaci(n)
end=time()
print(start-end)