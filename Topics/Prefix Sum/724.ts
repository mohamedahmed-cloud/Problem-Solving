function pivotIndex(nums: number[]): number {
    let n= nums.length 
    let s1 = 0, s2 = 0

    for (let i of nums) s2 += i

    s2 -= nums[0]
    for (let i = 1; i < n; i++) {
        if (s1 == s2) return i - 1
        s2 -= nums[i]
        s1 += nums[i - 1]
        
        
    }
    if (s1 == s2) return n - 1
    return -1
};
let nums = [-1, 1, 2]
console.log(pivotIndex(nums))