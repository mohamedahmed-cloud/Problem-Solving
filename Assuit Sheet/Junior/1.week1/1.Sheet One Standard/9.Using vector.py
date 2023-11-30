import sys,math
def solve(arr):
    for i in range(q):
        nums=list(map(str,sys.stdin.readline().split()))
        if nums[0]=="pop_back":
            arr=arr[:-1]
        elif nums[0]=="back":
            print(arr[-1])
        elif nums[0]=="front":
            print(arr[0])
        elif nums[0]=="push_back":
            arr.append(int(nums[1]))
        # If find error,error will start from here 
        elif nums[0]=="print":
            print(arr[int(nums[1])-1])
        elif nums[0]=="reverse":
            a,b=int(nums[1]),int(nums[2])
            a-=1
            arr[a:b]=reversed(arr[a:b])
        elif nums[0]=="sort":
            a,b=int(nums[1]),int(nums[2])
            a-=1
            arr[a:b]=sorted(arr[a:b])
n,q=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
# print(arr)
solve(arr)