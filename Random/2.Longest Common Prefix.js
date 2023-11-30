let solve1=function(strs){
    let to_loop=10000;
    n=strs.length;
    let s=""
    for(let i=0;i<n;i++){
        to_loop=Math.min(to_loop,strs[i].length);
    }
    for(let i=0;i<=to_loop;i++){
        s=strs[0].substring(0,i);
        strs.forEach(function(element){
            if(s==element.substring(0,i)){
                b=0
            }
            else{
                return s.substring(0,i-1)
            }
        })
    }
    return s
}
console.log(solve1(["flower","flow"]));