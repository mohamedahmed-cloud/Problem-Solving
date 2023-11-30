# passed all test case
def solve():
    a=Q%3
    if a ==1:
        print(A)
    elif a==2:
        print(B)
    else:
        print((A^B))
    
import sys
A,B,Q=map(int,sys.stdin.readline().split())
solve()