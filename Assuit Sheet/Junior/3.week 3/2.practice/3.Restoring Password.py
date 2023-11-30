main=int(input(),2)
arr={}
for i in range(10):
    arr[i]=int(input(),2)
print(arr)
arr=sorted(arr.items(),key=lambda x:x[1])
print(arr)
ans=""
for i in range(10):
    for j in arr:
        if j[0]==i:
            ans+=str(i)
print(ans)