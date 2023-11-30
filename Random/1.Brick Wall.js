/*
    Author : Mohamed Yousef 
    Date   : 2022-12-20
*/
let solve=function(wall){
    let defaultDict=new Proxy({},{
        get:(target,Name)=> Name in target?target[Name]:0
    });
    let ans=0
    n=wall.length;
    for(let i=0;i<n;i++){
        for(let j=0;j<wall[i].length;j++){
            if (j>0)
                wall[i][j]+=wall[i][j-1]
            defaultDict[wall[i][j]]+=1
        
    }
    }
    // console.log(wall[0].at(-1));
    for (let [key,value] of Object.entries(defaultDict)){
        if(key!=wall[0].at(-1)){
            ans=Math.max(value,ans)
        }
    }
    return n-ans
}
console.log(solve([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]));