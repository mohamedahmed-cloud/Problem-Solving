function decodeString(nums: string): string {
    let ans = ""
    let number= [], n = 0
    let str = [], st = ''

    for (let i of nums) {
        const curr = parseInt(i);
        if(!isNaN(curr)) {
            n = curr + 10 * n
        } else if(i == "[") {
            number.push(n)
            str.push(st)
            n = 0
            st = ''
        } else if(i == "]") {
            let tmp = st
            let currN;
            if(str.length > 0){
                let t = str.pop()
                if(t !== undefined) st = t
            } 
            if(number.length > 0) currN = number.pop()
            // console.log(tmp, st)
            while(currN && currN--) {
                st += tmp
            }
            // console.log(tmp, st)
        } else {
            st += i
        }
    }

    return st
}
// let nums = "3[a]2[bc]"
// console.log(decodeString(nums),  decodeString(nums) == "aaabcbc", "aaabcbc", )
