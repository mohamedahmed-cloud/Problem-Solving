/*
    Author : Mohamed Yousef 
    Date   : 2022-12-16
*/
let solve=function(nums){
    freq=Array(3).fill(0)
    nums.forEach(ele => {
        freq[ele]+=1
    })
    count=0
    for(let i=0;i<3;i++){
        while(freq[i]>0){
            freq[i]-=1
            nums[count]=i
            count+=1
        }
    }  
    return nums 
}
console.log(solve([2,0,2,1,1,0]));
