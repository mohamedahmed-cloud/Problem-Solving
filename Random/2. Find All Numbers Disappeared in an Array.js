/*
    Author : Mohamed Yousef 
    Date   : 2022-12-10
*/
let solve=function(nums){
    let n=nums.length;
    let freq=Array(n).fill(0)
    let s=new Set()
    nums.forEach(function(ele){
        freq[ele-1]+=1
    })
    for(let i=0;i<n;i++){
        if(freq[i]==0){
            s.add(i+1)
        }
    }
    return [...s]

}
console.log(solve([1,1]));