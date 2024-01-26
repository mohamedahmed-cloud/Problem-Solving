function findDifference(nums1: number[], nums2: number[]): number[][] {
    let ans = [], i = 0, j = 0
    let map = new Map()
    let n1 = nums1.length, n2 = nums2.length

    while (i < n1 && j < n2) {
        let val1 = map.get(nums1[i])
        map.set(nums1[i], val1? [val1[0] +1, val1[1]]: [1,0] )
        let val2 = map.get(nums2[j])
        map.set(nums2[j], val2? [val2[0], val2[1] + 1]: [0,1] )
        i ++; j ++;
    }
    while (i < n1) {
        let val1 = map.get(nums1[i])
        map.set(nums1[i], val1? [val1[0] +1, val1[1]]: [1,0] )
        i++
    }
    while (j < n2) {
        let val2 = map.get(nums2[j])
        map.set(nums2[j], val2? [val2[0], val2[1] + 1]: [0,1] )
        j++;
    }
    let ans1 = [], ans2 = []
    for (let [key, val] of map) {
        console.log(key, val)
        if (val[0] == 0 && val[1] >= 1) ans2.push(key)
        if (val[0] >= 1 && val[1] == 0) ans1.push(key)
    }
    
    ans.push(ans1)
    ans.push(ans2)
    return ans
};
let nums1 = [1,2,3,3], nums2 = [1,1,2,2]
console.log(findDifference(nums1, nums2))