def binaryRecursion(arr, l, r, key):
    '''
        This is the implementation for binary seach using recursion.
    '''
    mid = (l + r) //2
    if l > r:
        return -1
    
    if arr[mid] < key:
         return binaryRecursion(arr, mid + 1, r, key)
    elif arr[mid] > key:
        return binaryRecursion(arr, l, mid - 1, key)
    elif arr[mid] == key:
        return mid
    

arr = [1,2,3,5,6,7,8,8]
l = 0
r = len(arr) - 1

print(binaryRecursion(arr, l, r, 8))

def binaryIterative(arr, l, r, key):
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            r = mid -1
        elif arr[mid] < key:
            l = mid + 1
    return -1

print(binaryIterative(arr, l, r, 5))