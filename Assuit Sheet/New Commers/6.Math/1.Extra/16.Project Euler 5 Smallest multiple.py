# From Hackerrank
import sys,math
t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    number=1
    for j in range(1,n+1):
        number=math.lcm(j,number)
    print(number)