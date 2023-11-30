import sys,math
x1,y1,x2,y2=map(int,sys.stdin.readline().split())
x3,y3,x4,y4=map(int,sys.stdin.readline().split())
# Line One Equation is
# Cricle One
centerX1=(x1+x2)/2
centerY1=(y1+y2)/2
# Raduis One
RaduisOne=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))/2

# Cicle Two
centerX2=(x3+x4)/2
centerY2=(y3+y4)/2
# Raduis Two 
RaduisTwo =math.sqrt(math.pow(x3-x4,2)+math.pow(y3-y4,2))/2
# Distance between two raduis
distance=math.sqrt(math.pow(centerX1-centerX2,2)+math.pow(centerY1-centerY2,2))
if distance<=RaduisOne+RaduisTwo:
    print("YES")
else:print("NO")