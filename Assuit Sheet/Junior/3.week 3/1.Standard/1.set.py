import sys,bisect
def solve(a,b,arr):
    if a=="insert":
        bisect.insort(arr,b)
        # print(arr)
    elif a=="find":
        x=bisect.bisect_left(arr,b)
        try: 
            if arr[x]==b:
                return "found"
        except :return "not found"
        return "not found"
    elif a=="lower_bound":
        x=bisect.bisect_left(arr,b)
        try:return arr[x]
        except :return -1
    elif a=="upper_bound":
        try:
            x=bisect.bisect(arr,b)
            return arr[x]
        except:
            return -1

q=int(sys.stdin.readline())
arr=[]
for i in range(q):
    take=list(map(str,sys.stdin.readline().split()))
    c=solve(take[0],int(take[1]),arr)
    if c != None:
        print(c)