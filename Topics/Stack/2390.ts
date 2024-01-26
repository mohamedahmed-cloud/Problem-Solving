function removeStars(s: string): string {
    let stack: string[]= []
    for (let i of s) {
        if (i == "*") {
            stack.pop()
            continue
        }
        stack.push(i)
    }
    return stack.join("")
};
let s = "leet**cod*e"
console.log(removeStars(s))