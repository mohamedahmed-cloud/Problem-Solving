from bisect import bisect_left
def LIS(arr):
    stack = []
    for num in arr:
        if not stack or stack[-1] < num:
            stack.append(num)
        else:
            indx = bisect_left(stack, num)
            stack[indx] = num
    return len(stack)

arr = [0,1,0,3,2,3]
print(LIS(arr))
