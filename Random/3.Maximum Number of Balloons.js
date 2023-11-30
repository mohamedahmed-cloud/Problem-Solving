/*
    Author : Mohamed Yousef 
    Date   : 2022-12-10
*/
let solve=function(text){
    freq=Array(26).fill(0);
    for(let i=0;i<text.length;i++){
        freq[text[i].charCodeAt(0)-97]+=1

    }
    // return freq -> Balloon
    b=freq['b'.charCodeAt('b')-97]
    a=freq['a'.charCodeAt('a')-97]
    l=Math.floor(freq['l'.charCodeAt('l')-97]/2) //integer divsion
    o=parseInt(freq['o'.charCodeAt('o')-97]/2) //integer divison.
    n=freq['n'.charCodeAt('n')-97]
    return Math.min(a,b,l,o,n)
}
console.log(solve("balloon"));