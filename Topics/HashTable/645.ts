function findErrorNums(nums: number[]): number[] {
    let n = nums.length
    let ans = []
    let arr = new Array(n).fill(0)
    for (let i of nums) {
        if (arr[i - 1] == 1) ans.push(i)
        arr[i - 1] += 1
    }
    let cnt = 1
    for (let i of arr) {
        if (i == 0 ) {
            ans.push(cnt)
        }
        cnt += 1
    }
    // console.log(ans)
    return ans
};
let nums = [2, 2]
console.log(findErrorNums(nums))