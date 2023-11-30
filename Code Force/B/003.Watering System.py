import sys,math
n,A,B=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
s1=l[0]
sumall=l[0]
x=l[1:]
x.sort()
# print(x)
taken=0
for i in range(n):
    if i!=0:
        sumall+=x[i-1]
    if (s1*A)/sumall>=B:
        taken+=1
    else:break
print(n-taken)

