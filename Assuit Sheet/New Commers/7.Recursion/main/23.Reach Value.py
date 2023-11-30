def solve(n):
    if n==1:
        return 1
    if n<1:
        return 0
    check1= solve(n/10)
    check2= solve(n/20)
    return check1 or check2


import sys,math
t=int(sys.stdin.readline())
for i in range(t):
    a=solve(int(sys.stdin.readline()))
    if a :
        print("YES")
    else:print("NO")