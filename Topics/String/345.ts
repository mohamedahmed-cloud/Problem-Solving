function reverseVowels(s: string): string {
    let chck = new Set(["a", "A", "E", "e", "I", "i", "o", "O", "U", "u"])
    let order = []
    let ans = ""
    for(let i of s) {
        if (chck.has(i)) {
            order.push(i)
        }
    }
    let cnt = order.length - 1
    for(let i of s) {
        if (chck.has(i)) {
            ans += order[cnt]
            cnt -= 1
        }
        else {
            ans += i
        }
    }
    return ans

};
console.log(reverseVowels("hello"))