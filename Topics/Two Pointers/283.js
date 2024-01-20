"use strict";
/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums) {
    let cnt = 0;
    let n = nums.length;
    let curr = 0;
    for (let i = 0; i < n; i++) {
        if (nums[i] != 0) {
            nums[curr] = nums[i];
            curr++;
        }
        else {
            cnt++;
        }
    }
    let i = 1;
    while (cnt) {
        nums[n - i] = 0;
        cnt--;
        i++;
    }
    console.log(nums);
}
;
let nums = [0];
moveZeroes(nums);
