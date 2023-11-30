def binarySearch(arr,left,right,key):
    if left>right:
        return -1
    mid=(left+right)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return binarySearch(arr,left,mid-1,key)
    elif arr[mid]<key:
        return binarySearch(arr,mid+1,right,key)

import sys
arr=list(map(int,sys.stdin.readline().split()))
# print(arr)
left=0
right=len(arr)-1
key=10
print(binarySearch(arr,left,right,key))