import sys
x1,y1,x2,y2=map(int,sys.stdin.readline().split())
x3,y3,x4,y4=map(int,sys.stdin.readline().split())
if (y2-y1)*(x4-x3)==(x2-x1)*(y4-y3):
    print("YES")
else:print("NO")