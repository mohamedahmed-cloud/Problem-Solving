"use strict";
function predictPartyVictory(senate) {
    let rest = [];
    let map = { D: "Dire", R: "Radiant" };
    let n = senate.length;
    let Darr = [];
    let Rarr = [];
    for (let i = 0; i < n; i++) {
        if (senate[i] == "D")
            Darr.push(i);
        else
            Rarr.push(i);
    }
    while (Darr.length && Rarr.length) {
        if (Darr[0] < Rarr[0]) {
            Darr.push(n);
        }
        else {
            Rarr.push(n);
        }
        n += 1;
        Darr.shift();
        Rarr.shift();
    }
    console.log(Darr, Rarr);
    return Darr.length ? map["D"] : map["R"];
}
let senate = "RD";
console.log(predictPartyVictory(senate));
