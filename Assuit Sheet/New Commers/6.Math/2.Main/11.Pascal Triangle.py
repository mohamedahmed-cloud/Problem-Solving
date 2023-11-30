def combination(n,r):
    ans=1
    out=1     
    for i in range(n-r+1,n+1):
        ans*=i 
    for i in range(2,r+1):
        out*=i  
    return ans//out
import sys
n=int(sys.stdin.readline())
for i in range(0,n):
    for j in range(0,i+1):
        print(combination(i,j),end=' ')
    print()
