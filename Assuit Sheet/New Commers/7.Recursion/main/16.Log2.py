# It give a round number so it's not accepted
# first solution 
# def log2(left,right,n,ans,iter):
#     iter+=1
#     if iter>100:
#         return (left+right)/2
#     mid=(left+right)/2
#     if math.pow(2,mid)==n:
#         return mid
#     elif math.pow(2,mid)>n:
#         return log2(left,mid,n,ans,iter+1)
#     elif math.pow(2,ans)<n:
#         return log2(mid,right,n,ans,iter+1)

# import sys,math
# n=int(sys.stdin.readline())
# ans=0
# left=0
# right=n
# iter=0
# out=log2(left,right,n,ans,iter)
# if out<10e-7:
#     print(0)
# elif n%2==0:
#     print(int(math.ceil(out)))
# elif float(int(out))==out:
#     print(int(out))
# else:print(out)


# second solution 

import math 
a=math.log2(int(input()))
print(int(a))


n=int(input())
ans=0
def solve2(n,ans):
    if n==1:
        return ans
    ans+=1
    return solve2(n//2,ans)
print(solve2(n,ans))
