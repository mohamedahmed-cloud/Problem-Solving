function bisect_left(nums: number[], val: number, l: number, r: number): number {
    while (l < r) {
        const mid = (l + r) >> 1
        if (nums[mid] < val) {
            l = mid + 1;
        }
        else {
            r = mid 
        }
    }

    return l
}
function increasingTriplet(nums: number[]): boolean {
    let ans: number[] = []
    let r = 0

    for(let i of nums) {
        if (!ans.length || ans.slice(-1)[0] < i)
        {
            ans.push(i)
            r += 1
        }else  {
            let indx = bisect_left(ans, i, 0, r)
            ans[indx] = i
        }
        if (r >= 3) return true

    }
    return false
}

let numss = [20,100,10,12,5,13]
console.log(increasingTriplet(numss))

// another solution 

function increasingTriplet(nums: number[]): boolean {
    let n1 = Infinity
    let n2 = Infinity
    for (const num of nums) {
        if (num <= n1) n1 = num
        else if (num <= n2) n2 = num
        else return true
    }
    return false
};