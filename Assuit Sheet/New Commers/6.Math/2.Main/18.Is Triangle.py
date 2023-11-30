def solve(x,y,z):
    arr=[x,y,z]
    check=[x+y,x+z,y+z]
    # print(check)
    for i in arr:
        for j in check:
            if i>=j:
                # print(i,j)
                return "Invalid"
    my_area=area(x,y,z)
    return "Valid",my_area
def area(x,y,z):
    s=(x+y+z)/2 
    return math.sqrt(s*(s-x)*(s-y)*(s-z))
import math,sys
x,y,z=map(int,sys.stdin.readline().split())
a=solve(x,y,z)
if a=="Invalid":
    print(a)
else:
    print(a[0])
    print("{:.8f}".format(a[1]))