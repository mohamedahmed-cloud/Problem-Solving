/*
    Author : Mohamed Yousef 
    Date   : 2022-12-16
*/
let solve=function(nums){
    let numSet=new Set(nums);
    longest=0
    console.log(numSet);
    numSet.forEach(ele => {
        if(numSet.has(ele-1)==false){
            length=0
            while(numSet.has(ele+length)==true){
                length++;
            }
            longest=Math.max(length,longest)
        }
    })
    return longest
}
console.log(solve([-1,-9,-5,-2,-9,8,-8,1,-9,-3,-3]));