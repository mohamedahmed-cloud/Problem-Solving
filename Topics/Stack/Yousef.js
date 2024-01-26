"use strict";
function Yousef(nums) {
    let ans = "";
    let number = [], n = 0;
    let str = [], st = "";
    for (let i of nums) {
        const curr = parseInt(i);
        if (!isNaN(curr)) {
            n = curr + 10 * n;
        }
        else if (i == "[") {
            number.push(n);
            str.push(st);
            n = 0;
            st = "";
        }
        else if (i == "]") {
            let tmp = st;
            let currN = 0;
            if (str.length > 0)
                st = str.pop();
            if (number.length > 0)
                currN = number.pop();
            while (currN && currN--) {
                st += tmp;
                tmp = st;
            }
        }
        else {
            st += i;
        }
    }
    // console.log(n, number)
    return ans;
}
