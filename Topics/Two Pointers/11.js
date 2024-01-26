"use strict";
function maxArea(height) {
    let p1 = 0;
    let n = height.length;
    let p2 = n - 1;
    let ans = 0;
    while (p2 >= p1) {
        ans = Math.max(ans, Math.min(height[p1], height[p2]) * (n - 1));
        if (height[p1] > height[p2]) {
            p2--;
        }
        else {
            p1++;
        }
        n--;
    }
    return ans;
}
;
let height = [1, 1];
console.log(maxArea(height));
