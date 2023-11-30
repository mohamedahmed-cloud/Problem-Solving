/*
    Author : Mohamed Yousef 
    Date   : 2023-01-07
*/
let solve=function(gas,cost){
    let start=0;
    let now=0
    profit=0
    n=gas.length;
    for(let i=0;i<n;i++){
        profit+=(gas[i]-cost[i])
        now+=(gas[i]-cost[i])
        if(now<0){
            now=0
            start=i+1
        }
    }
    // console.log(start);
    return profit<0 ? -1: start;
}
console.log(solve([1,2,3,4,5],[3,4,5,1,2]));