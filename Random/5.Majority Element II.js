/*
    Author : Mohamed Yousef 
    Date   : 2022-12-03
*/
let solve=function (nums){
    let x=nums.length;
    let over=Math.floor(x/3);
    let add="hi"
    repeated=1
    list=new Set()
    nums.sort(function(a,b){
        return a-b
    })
    if(x==1 || x==2){
        let out=new Set(nums)
        return [...out]
    }
    for(let i=0; i<x-1; i++){
        if (nums[i]==nums[i+1]){
            add=nums[i]
            repeated+=1
        }else {
            if(repeated>over){
                list.add(nums[i])
            }
            repeated=1
        }
    }
    if (repeated>over && add!="hi"){
        list.add(add)
    }
    return [...list]
}
console.log(solve([3,3,4]));
