def solve(arr):
    n=len(arr)
    ans=[0]*n
    x=-1
    if n>=2:
        ans[-1]=-1
        ans[-2]=arr[-1]
        x=max(arr[-2],arr[-1])
    for i in range(n-3,-1,-1):
        x=max(arr[i+1],x)
        ans[i]=x
    ans[-1]=-1
    return ans
print(solve([17,18,5,4,6,1]))