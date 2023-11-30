import sys
x1,y1,x2,y2,x3,y3,x4,y4=list(map(int,sys.stdin.readline().split()))
n=int(sys.stdin.readline())

# Arrays
arrX=[x1,x2,x3,x4] 
arrY=[y1,y2,y3,y4]
# My Border 
maxX=max(arrX)
minX=min(arrX)

maxY=max(arrY)
minY=min(arrY)
print(maxX,minX,maxY,minY)
for i in range(n):
    x,y=list(map(int, sys.stdin.readline().split()))
    if maxX>=x and maxY>=y and minX<=x and minY<=y:
        print("YES")
    else:print("NO")
    


