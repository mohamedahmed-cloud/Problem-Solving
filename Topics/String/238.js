"use strict";
function productExceptSelf(nums) {
    let mul = 1;
    let zero = 0;
    for (let i of nums) {
        if (i != 0) {
            mul *= i;
        }
        else {
            zero += 1;
        }
    }
    let ans = [];
    for (let i of nums) {
        if (zero >= 1) {
            if (i != 0 || zero > 1)
                ans.push(0);
            else
                ans.push(mul);
        }
        else {
            ans.push(mul / i);
        }
    }
    return ans;
}
;
let nums = [-1, 1, 0, -3, 3];
console.log(productExceptSelf(nums));
