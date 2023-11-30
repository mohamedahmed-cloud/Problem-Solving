def Reach_Value(ans,n,arr,my_index,x):
    if my_index ==n:
        return ans==x
    check1=Reach_Value(ans - arr[my_index],n,arr,my_index+1,x)
    check2=Reach_Value(ans+arr[my_index],n,arr,my_index+1,x)
    return check1 or check2
    
import sys,math
n,x=map(int, sys.stdin.readline().split())
arr =list(map(int,sys.stdin.readline().split()))
ans=arr[0]
my_index=1
if Reach_Value(ans,n,arr,my_index,x):
    print("YES")
else:print("NO")
