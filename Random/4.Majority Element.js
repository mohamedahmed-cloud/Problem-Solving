/*
    Author : Mohamed Yousef 
    Date   : 2022-12-03
*/
let solve=function(nums){
    nums.sort(function(a,b){
        return a-b
    })
    let repeated=1
    let maxelement=0
    x=0
    y="h"
    for(let i=1;i<nums.length;i++){
        if(nums[i-1]==nums[i]){
            x=nums[i]
            repeated+=1
        }
        else repeated=1
        if (repeated>maxelement) {
            maxelement=repeated
            y=x
        }
    }
    return (y!="h")? y :nums[0]
}

console.log(solve([2,3,3]));

