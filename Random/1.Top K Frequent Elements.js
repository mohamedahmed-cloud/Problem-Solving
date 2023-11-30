/*
    Author : Mohamed Yousef 
    Date   : 2022-12-14
*/
let solve=function(nums,k){
    let defaultDict=new Proxy({},{
        get:(target,Name) => Name in target?target[Name]:0
    });
    nums.forEach(ele => {
        defaultDict[ele]+=1
    })
    // sort default dict
    //First create an array from Object 
    let item=Object.keys(defaultDict).map(function(key){
        return [key,defaultDict[key]]
    })
    item.sort(function(a,b){
        return b[1]-a[1]
    })
    // return item
    ans=[]
    for(let i=0;i<k;i++) {
        ans.push(parseInt(item[i][0]))
    }
    return ans
}
console.log(solve([1,1,1,2,2,2,2,3,3], 2));