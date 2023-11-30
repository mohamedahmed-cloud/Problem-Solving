def solve(nums):
    nums.sort()
    n=len(nums)
    for i in range(1,n):
        if nums[i-1]==nums[i]:
            return True
    return False
print(solve([1,2,3]))

def solve2(nums):
    from collections import Counter
    l=Counter(nums).most_common()
    # print(l)
    for i in l:
        if i[1]>1:
            return True
    return False
print(solve2([1,2,3,4,1]))