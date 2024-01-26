"use strict";
function removeStars(s) {
    let stack = [];
    for (let i of s) {
        if (i == "*") {
            stack.pop();
            continue;
        }
        stack.push(i);
    }
    return stack.join("");
}
;
let s = "leet**cod*e";
console.log(removeStars(s));
