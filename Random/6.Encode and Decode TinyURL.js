/*
    Author : Mohamed Yousef 
    Date   : 2022-12-16
*/
let mapping={};
let encode=function(longUrl){
    let count=0;
    let shortenUrl=""
    let l=longUrl.split("/")
    l.forEach(ele => {
        if(ele===""){
            ele="/";
        }
        mapping[""+count]=ele;
        shortenUrl+=""+count;
        count+=1;
    })
    
    return shortenUrl
}
let decode=function(shortUrl){
    let ans="";
    for (let i of shortUrl){
        ans+=mapping[i]
        if(mapping[i]!="/"){
            ans+="/"
        }
    }
    return ans.slice(0,ans.length-1)
}
console.log(encode("https://leetcode.com/problems/design-tinyurl"))

// --------------------------------------------
// another solution with js we can use Buffer to encode and deconde
let encode2=function(longUrl){
    let shortUrl=Buffer.from(longUrl,"binary")
    return decode2(shortUrl) //change this to 
    // return shortUrl  to run in leetcode
}
let decode2=function(shortUrl){
    return shortUrl.toString()
}