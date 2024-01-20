"use strict";
function isSubsequence(s, t) {
    let n1 = s.length, n2 = t.length;
    let i = 0, j = 0;
    while (i < n1 && j < n2) {
        if (s[i] == t[j]) {
            i++;
            j++;
        }
        else
            j += 1;
    }
    return i == n1;
}
;
let s = "abcd";
let t = "ahbgdc";
console.log(isSubsequence(s, t));
