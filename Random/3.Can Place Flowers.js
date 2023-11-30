/*
    Author : Mohamed Yousef 
    Date   : 2022-12-03
*/
let solve=function(flowerbed,n){
    x=flowerbed.length
    if (x==1){
        if (flowerbed[0]==1) {
            if (n==0) return true
            return false
        }
        return true
    }
    if (flowerbed[0]==flowerbed[1]){
        flowerbed[0]=1
        n-=1
    }
    for(let i=1;i<x-1;i++){
        if(flowerbed[i]==0 && flowerbed[i+1]==0 && flowerbed[i-1]==0){
            n-=1
            flowerbed[i]=1
        }
    }
    if (flowerbed.at(-1)==flowerbed.at(-2)){
        flowerbed[0]=1
        n-=1
    }
    if (n<=0) return true
    return false
}
console.log(solve([1,0,0,0,1],1));