/*
    Author : Mohamed Yousef 
    Date   : 2022-12-07
*/
let solve=function(nums1,nums2){
    let n=nums2.length;
    let stack=[];
    let out=[];
    let ans=Array(n).fill(-1);
    for(let i=0;i<n;i++){
        while ( stack.length!=0 && nums2[i]>nums2[stack.at(-1)]){
            
            ans[stack.at(-1)]=i;
            stack.pop()    
        }
        stack.push(i);
    }
    // console.log(ans);
    nums1.forEach(function(ele){
        function checkIndex(index){
            return index == ele
        }
        // console.log(nums2.findIndex(checkIndex));
        let x=ans[nums2.findIndex(checkIndex)]
        if(x==-1){
            out.push(x)
        }else {
            out.push(nums2[x])
        }

    })
    return out
}
console.log(solve([4,1,2],[1,3,4,2]));