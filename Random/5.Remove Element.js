let solve=function(nums,val){
    n=nums.length;
    k=0
    for(let i=0;i<n;i++){
        if(nums[i] !=val ){
            nums[k]=nums[i] 
            k++
        }
    }
    return k
}
console.log(solve([1,2,3,33,3],3));