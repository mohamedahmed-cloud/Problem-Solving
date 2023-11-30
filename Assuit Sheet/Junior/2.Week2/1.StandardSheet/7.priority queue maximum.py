import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    take=sys.stdin.readline().split()
    if take[0] =="push":
        arr.insert(int(take[1]),int(take[1]))
    elif take[0]=="pop":
        arr.remove(max(arr))
    elif take[0]=="top":
        print(max(arr))
    # print(arr)



