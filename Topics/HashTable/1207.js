"use strict";
function uniqueOccurrences(arr) {
    let map = new Map();
    let set = new Set();
    for (let i of arr) {
        map.set(i, (map.get(i) || 0) + 1);
    }
    for (let [key, val] of map) {
        if (set.has(val)) {
            return false;
        }
        set.add(val);
    }
    return true;
}
;
let arr = [1, 2];
console.log(uniqueOccurrences(arr));
