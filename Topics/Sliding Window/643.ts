function findMaxAverage(nums: number[], k: number): number {
    let p1 = 0
    let n = nums.length
    let ans = 0
    let curr = 0
    for (let i = 0; i < k; i++) {
        curr += nums[i]
    }
    ans = curr
    for (let i = k ; i < n; i++ ) {
        curr += nums[p1] * -1
        curr += nums[i]
        ans = Math.max(curr, ans)
        p1++;
    }
    console.log(ans)
    return  Number((ans / k).toFixed(5))
};


let nums = [0,1,1,3,3], k = 4
console.log(findMaxAverage(nums, k))