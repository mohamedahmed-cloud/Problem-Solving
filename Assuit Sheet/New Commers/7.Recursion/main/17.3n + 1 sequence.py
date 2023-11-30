def solve(n,iteration):
    if n==1:
        return iteration
    while n!=1:
        iteration+=1
        if n%2==0:
            n=n/2
        elif n%2!=0:
            n=3*n+1
    return iteration
import sys
n=int(sys.stdin.readline())
iteration=1
print(solve(n,iteration))
        
