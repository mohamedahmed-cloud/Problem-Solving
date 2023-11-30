
import sys,math,functools
p= [ 0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0 ]

t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    if p[n-1]:
        print("prime")
    else:print("not prime")
    # x=Fibonacci(n)
    # y=prime(x)
    # print(y)

# This Give me a time limit so that I make a array of 50th fib number 

# def prime(n):
#     if n==0 or n==1:
#         return "not prime"
#     for i in range(2,int(math.sqrt(n))+1):
#         if n%i==0:
#             return "not prime"
#     return "prime"

# def Fibonacci(n):
#     n1=0
#     n2=1
#     n3=1
#     for i in range(2,n):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#     return n3