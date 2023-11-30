/*
    Author : Mohamed Yousef 
    Date   : 2022-12-07
*/
let solve=function(nums){
    let n=nums.length;
    let sum1=0
    // let i=0
    s=nums.slice(1,n)
    if (n==1) return 0
    let sum2=s.reduce((ele1,ele2)=>ele1+ele2)
    for(var i=1;i<n;i++){
        if (sum1==sum2){
            return i-1
        }
        console.log(`${sum1} ${sum2}`)
        sum1+=nums[i-1]
        sum2-=nums[i]
    }
    if (sum1==sum2) return i-1
    return -1
}
console.log(solve([1,0]));
