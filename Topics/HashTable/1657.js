"use strict";
function closeStrings(word1, word2) {
    let n1 = word1.length, n2 = word2.length;
    let map1 = {}, map2 = {};
    if (n1 !== n2)
        return false;
    for (let i = 0; i < n1; i++) {
        map1[word1[i]] = (map1[word1[i]] || 0) + 1;
        map2[word2[i]] = (map2[word2[i]] || 0) + 1;
    }
    for (let key1 in map1) {
        let flag = true;
        for (let key2 in map2) {
            if (map1[key1] == map2[key2] && map2.hasOwnProperty(key1)) {
                map2[key2] = 0;
                flag = false;
                break;
            }
        }
        if (flag)
            return false;
    }
    return true;
}
;
let word1 = "aax", word2 = "ssu";
console.log(closeStrings(word1, word2));
