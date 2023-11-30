def solve(x1,y1,x2,y2):
    a=math.pow(abs(x1-x2),2)
    b=math.pow(abs(y1-y2),2)
    return math.sqrt(a+b)

import sys,math
x1,y1,x2,y2=map(int,map(int,sys.stdin.readline().split()))
ans=solve(x1,y1,x2,y2)
print("{:.9f}".format(ans))