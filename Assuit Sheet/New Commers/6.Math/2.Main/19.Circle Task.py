def solve(x,y,r,p):
    arr=[]
    for i in range(p):
        a,b=map(int,sys.stdin.readline().split())
        # find the distance from the center to the point and compare them 
        if (x-a)**2 +(b-y)**2<=r**2:
            print("YES")
        else:print("NO")
import sys,math
x,y,r,p=map(int,sys.stdin.readline().split())
arr=solve(x,y,r,p)
# for i in arr:
#     print(i)