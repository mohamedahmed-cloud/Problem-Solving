import math
n=int(input())
arr=[]
x=2
for i in range(1,int(math.sqrt(n))+1):
    while n%x==0 and n>1:
        arr.append(x)
        n=n//x
    else:
        x+=1
if n!=1:
    arr.append(n)
print(*arr)
        # print(x)