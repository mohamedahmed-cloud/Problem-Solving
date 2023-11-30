def trivial_solution(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def solve(nums,target):
    our_dict={}
    for i,value in enumerate(nums):
        x=target-value
        if x in our_dict:
            return [our_dict[x],i]
        our_dict[value]=i
        
print(solve([1,2,9,12,3],4))