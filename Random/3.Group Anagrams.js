let solve=function(strs){
    /*to sort string
    (str.split("").sort()).join("")
     */
    sorted_string=[]
    out=[]
    let inarr=function(x){
        for(let i=0;i<sorted_string.length;i++){
            if (x==sorted_string[i]) return i
        }
        return -1
    }
    strs.forEach(function(ele){
        x=(ele.split("").sort()).join("")
        b=inarr(x)
        if (b==-1){
            out.push([ele])
            sorted_string.push(x)
        }else {
            out[b].push(ele)
        }
    })
    return out
}
console.log(solve(["eat","tea","tan","ate","nat","bat"]))