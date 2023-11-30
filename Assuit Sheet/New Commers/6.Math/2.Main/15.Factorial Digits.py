import math
def solve(num):
    # ans=1
    # for i in range(2,num+1,2):
    #     if i<num: 
    #         ans*=i*(i+1)
    #     else:ans*=i
    length=len(str(math.factorial(num)))
    return "Number of digits of "+str(num)+"!"+" is "+str(length)
def solve2():
    # more fastest the first one
    ans=0
    for i in range(2,num+1):
        ans+=math.log10(i) 
    return"Number of digits of "+ str(num)+"!"+" is "+str(int(math.ceil(ans)))

num=int(input())
# print(solve(num))
print(solve2())