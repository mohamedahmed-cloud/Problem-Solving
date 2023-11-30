/*
    Author : Mohamed Yousef 
    Date   : 2022-12-10
*/
let solve=function(pattern,s){
    s=s.split(" ");
    n=pattern.length;
    m=s.length;
    if (n!=m) return false;
    // default dict1 in js
    let dict1=new Proxy({},{
        get:(object,Name) => Name in object? object[Name] : 0
    })
    // Default dict2 in js
    let dict2=new Proxy({},{
        get:(object,Name) => Name in object? object[Name]:0
    })
    for(let i=0;i<n;i++){
        for([ele,x] of Object.entries(dict1)){
            if (ele==s[i] && x!=pattern[i]) return false;
        }
        for([ele,x] of Object.entries(dict2)){
            if (ele==pattern[i] && x!=s[i]) return false;
        }
        dict1[s[i]]=pattern[i];
        dict2[pattern[i]]=s[i];
    }
    return true;
}
console.log(solve("abba","dog cat cat dog"));