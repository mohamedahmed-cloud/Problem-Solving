function predictPartyVictory(senate: string): string {
  let rest: string[] = [];
  let map: Record<string, string> = { D: "Dire", R: "Radiant" };
  
  
    let n = senate.length
    let Darr: Array<number> = [];
    let Rarr: Array<number> = [];

    for (let i = 0 ; i < n; i ++) {
        if (senate[i] == "D") Darr.push(i)
        else Rarr.push(i)
    }

    while (Darr.length && Rarr.length) {
        if(Darr[0] < Rarr[0]) {
            Darr.push(n)
        } else  {
            Rarr.push(n)
        }
        n += 1
        Darr.shift()
        Rarr.shift()
    }
    console.log(Darr, Rarr)
    return Darr.length? map["D"]: map["R"];
}
let senate = "RD";
console.log(predictPartyVictory(senate));
