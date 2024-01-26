"use strict";
function longestOnes(nums, k) {
    let p1 = 0, p2 = 0, ans = 0, curr = 0;
    let n = nums.length;
    while (p2 < n) {
        if (nums[p2] == 0) {
            if (k == 0) {
                if (nums[p1] == 0)
                    k += 1;
                p1 += 1;
                curr -= 1;
            }
            else {
                p2 += 1;
                k -= 1;
                curr += 1;
                if (curr > ans)
                    ans = curr;
            }
        }
        else {
            curr += 1;
            if (curr > ans)
                ans = curr;
            p2 += 1;
        }
    }
    return ans;
}
;
let numss = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], ks = 3;
console.log(longestOnes(numss, ks));
