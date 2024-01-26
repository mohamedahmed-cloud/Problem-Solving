function largestAltitude(gain: number[]): number {
    let n = gain.length
    let prefix = 0, ans = 0

    for(let i of gain) {
        prefix += i
        if (prefix > ans) ans = prefix 
    }
    return ans
};
let gain = [-5,1,5,0,-7]
console.log(largestAltitude(gain))
