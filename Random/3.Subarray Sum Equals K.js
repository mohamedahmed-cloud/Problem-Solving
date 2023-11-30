/*
    Author : Mohamed Yousef 
    Date   : 2023-01-05
*/
let solve=function(nums,k){
    let defaultDict=new Proxy({},{
        get:(target,name)=>name in target?target[name]:0
        
    })
    defaultDict[0]=1
    let sum=0
    let ans=0
    for(let i of nums){
        sum+=i
        ans+=defaultDict[sum-k]
        defaultDict[sum]+=1
    }
    return ans;
}
console.log(solve([1,1,1],2));