#    Author : Mohamed Yousef 
#    Date   : 2022-12-03
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
# Solving by Sort algorithm
def solve(nums):
    nums.sort()
    x=len(nums)
    # print(x)
    over=x//3
    ans=set()
    repeated=1
    to_add="hi"
    if x==2 or x==1:return list(set(nums))
    for i in range(x-1):
        if nums[i]==nums[i+1]:
            to_add=nums[i]
            repeated+=1
        else:
            if repeated>over:
                # print(repeated,over)
                ans.add(nums[i])
            repeated=1
    if repeated>over and to_add!="hi" :
        ans.add(to_add)
    return list(ans)
print(solve([1,1,2,2,1,1,1,1,2,2,1,1]))
# Solving by Hashing table.
def solvehash(nums):
    x=defaultdict(int)
    n=len(nums)
    over=n//3
    add=set()
    for i in nums:
        x[i]+=1
    for key,value in x.items(): 
        if value>over:
            add.add(key)
    return list(add)
        

print(solvehash([1,2]))
# Time complexity -> O(n)
# space complexity -> O(1)
def boyerMoore(nums):
    num1=-1
    c1=0
    num2=-1
    c2=0
    n=0
    for i in nums:
        n+=1
        if num1==i:c1+=1
        elif num2==i:c2+=1
        elif c1==0:
            num1=i
            c1=1
        elif c2==0:
            num2=i
            c2=1
        else:
            c1-=1
            c2-=1
    check1=0
    check2=0
    for i in nums:
        if num1==i:check1+=1
        if num2==i:check2+=1
    over=n//3
    if check1>over and check2>over and num1!=num2:
        return [num1,num2]
    elif check2>over:
        return [num2]
    elif check1>over:
        return [num1]
    return []

print(boyerMoore([-1,-1,-1]))


