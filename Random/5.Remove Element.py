def solve(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)
def solve2(nums,val):
    n=len(nums)
    k=0
    for i in range(n):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k
print(solve2([1,2,3,3,2,2,2,2,2],2))