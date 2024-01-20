"use strict";
function compress(chars) {
    let indx = 1;
    let n = chars.length;
    let cnt = 1;
    let ans = 0;
    for (let i = 1; i <= n; i++) {
        if (i < n && chars[i] == chars[i - 1]) {
            cnt += 1;
        }
        else {
            if (cnt > 1) {
                let str = `${cnt}`.split("");
                chars[indx - 1] = chars[i - 1];
                for (let j of str) {
                    chars[indx] = j;
                    indx += 1;
                }
                ans += str.length;
            }
            else {
                chars[indx - 1] = chars[i - 1];
            }
            ans += 1;
            cnt = 1;
            indx += 1;
        }
    }
    console.log(chars);
    return ans;
}
let chars = ["a", "a", "a", "a", "a", "b"];
console.log(compress(chars));
