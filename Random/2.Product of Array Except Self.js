/*
    Author : Mohamed Yousef 
    Date   : 2022-12-14
*/
let solve=function(nums){
    n=nums.length;
    ans=Array(n).fill(1)
    pre=1
    i=0
    nums.forEach(function(ele){
        ans[i]=pre
        pre*=ele
        i++;
    })
    post=1
    for(let i=n-1;i>=0;i--){
        ans[i]*=post
        post*=nums[i]
    }
    return ans
}
console.log(solve( [-1,1,0,-3,3]));