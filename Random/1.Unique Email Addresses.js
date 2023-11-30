let solve=(emails)=>{
    let ans=new Set()
    emails.forEach((big)=> {
        let after=0
        let plus=0
        let to_add=""
        for(let i=0;i<big.length;i++){
            small=big[i]
            if(small=="@"){
                after="@"
            }
            if (small=="+"){
                plus="+"
            }else if (after==0 && small=="."){
                x=0
            }
            else if (plus==0 || after=="@"){
                to_add+=small
            }
        }
        ans.add(to_add)
    })
    return ans.size
}
console.log(solve(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]));