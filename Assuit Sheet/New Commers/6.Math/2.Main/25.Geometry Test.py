import sys,math
R,S=map(int,sys.stdin.readline().split())
if R*math.sqrt(2)>=S:
    print("Circle")
elif R<=S/2:
    print("Square")
else :
    print("Complex")
