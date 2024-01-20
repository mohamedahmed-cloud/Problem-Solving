"use strict";
function kidsWithCandies(candies, extraCandies) {
    let mx = Math.max(...candies);
    let n = candies.length;
    let ans = [];
    for (let i of candies) {
        if (i + extraCandies >= mx)
            ans.push(true);
        else
            ans.push(false);
    }
    return ans;
}
;
