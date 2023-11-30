import sys,math
x,y=map(int, sys.stdin.readline().split())
my_dict={}
for i in range(x):
    name,money=map(str,sys.stdin.readline().split())
    my_dict[name]=int(money)
for i in range(y):
    arr=list(map(str,sys.stdin.readline().split()))
    if arr[0]=="1":
        # print(my_dict[arr[1]],arr[2],type(arr[2]),int(arr[2]))
        my_dict[arr[1]]+=int(arr[2])
    else:
        print(my_dict[arr[1]])

