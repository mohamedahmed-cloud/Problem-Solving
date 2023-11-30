// This Solution get Runtime Error I don't know why...
// The test it throw exception i try on vscode it run well and didn't get any error.
let solution = function (nums, target) {
  our_dict = {};
  n = nums.length;
  let out=0
  for (let i = 0; i < n; i++) {
    let x = target - nums[i];
    if (x === 0) {
      out = i;
      break;
    }
    Object.keys(our_dict).forEach((key) => {
      if (key == x) out = [our_dict[key], i];
    });
    our_dict[nums[i]] = i;
  }
  return out;
};
console.log(solution([0, 2, 3, 0], 0));
// another solution 
let solve2=function(nums,target){
  n=nums.length;
  for(let i=0;i<n;i++){
    for(let j=i+1;j<n;j++){
      if(nums[i]+nums[j]==target){
        return [i,j]
      }
    }
  }
}
console.log(solve2([3,2,4],6))

// another solution with map
let solve3=function(nums,target,map=new Map()){
  n=nums.length;
  for(let i=0;i<n;i++){
      x=target-nums[i]
      y=map.get(x)
      z=map.has(x)
      if(z) return [y,i]
      map.set(nums[i],i)
  }
}
console.log(solve3([3,2,4,1],4))