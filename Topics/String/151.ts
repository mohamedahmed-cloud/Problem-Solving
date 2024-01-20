function reverseWords(s: string): string {
    s = s.trim()
    let l = s.split(" ")
    let n = l.length
    let ans = ""
    // console.log(l)
    for (let i = n - 1; i >= 0; i--) {
        if(l[i] != "") {
            // console.log(l[i])
            ans += l[i] + " "

        }
    }
    return ans.slice(0, ans.length - 1)
};


let s = "a good             example"
console.log(reverseWords(s))