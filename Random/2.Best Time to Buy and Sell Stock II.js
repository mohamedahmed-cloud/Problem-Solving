/*
    Author : Mohamed Yousef 
    Date   : 2022-12-23
*/
let solve=function(prices){
    let n=prices.length;
    buy=-1
    profit=0
    for(let i=1;i<n;i++){
        if(prices[i]>prices[i-1] && buy==-1){
            buy=prices[i-1]
        }
        if (buy>=0 && prices[i]>prices[i+1]){
            profit+=prices[i]-buy
            buy=-1
        }

    }
    if (buy>=0 && prices.at(-1)>buy){
        profit+=prices.at(-1)-buy
    }
    return profit;
}
console.log(solve([7,6,4,3,1]));