// solution with hashmap

function maxOperations(nums: number[], k: number): number {
    let ans = 0
    let map = new Map()

    for (let i of nums) map.set(i, (map.get(i) || 0) + 1)
    
    // console.log(map)
    for(let i of nums)
    {
        const tmp = k - i
        if (map.get(tmp) > 0) {
            map.set(tmp, map.get(tmp) - 1)
            if (map.get(i) > 0)
            {
                map.set(i, map.get(i) - 1)
                ans += 1
            }
        }
    }
    return ans
};

// console.log(maxOperations(numss, k))

// solution with two pointer

function maxOperationss(nums: number[], k: number): number {
    let ans = 0
    let p1 = 0
    let p2 = nums.length - 1
    nums.sort((a, b) => a - b)
    // console.log(nums)


    while (p2 > p1) {
        // console.log(p2, p1)
        if (nums[p1] + nums[p2]  == k)
        {
            p1 ++;
            p2 --;
            ans += 1
        } else if (nums[p1] + nums[p2] > k) p2 --
        else p1++
    }
    return ans
};
let numss = [3,1,3,4,3]
let k = 6

console.log(maxOperationss(numss, k))