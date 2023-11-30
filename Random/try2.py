nums = [2, 4, 6, "prevent", 10]
curr = 2
for i in range(len(nums)):
    if nums[i] != "prevent" and nums[i] % nums[i] == 0 and nums[i] != 1:
        print("Found a multiple of nums[curr] at index", i)