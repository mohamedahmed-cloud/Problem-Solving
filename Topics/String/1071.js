"use strict";
function gcdOfStrings(str1, str2) {
    let n1 = str1.length, n2 = str2.length;
    if (str1 + str2 !== str2 + str1) {
        return "";
    }
    let gcdNumber = gcd(n1, n2);
    // console.log(gcdNumber)
    return str1.slice(0, gcdNumber);
}
;
function gcd(n1, n2) {
    if (n2 == 0)
        return n1;
    return gcd(n2, n1 % n2);
}
let str1 = "ABC";
let str2 = "ABCABC";
console.log(gcdOfStrings(str1, str2));
