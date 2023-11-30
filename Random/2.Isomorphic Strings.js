/*
	Author : Mohamed Yousef 
	Date   : 2022-12-02
*/
let solve=(t,s) => {
    n1=s.length;
    n2=t.length;
    if (n1 !=n2) return false;
	let defaultdict1=new Proxy({},{
		get :(target,Name) => Name in target? target[Name] : 0
	})
	let defaultdict2=new Proxy({},{
		get :(target,Name) => Name in target? target[Name] : 0
	})
	// map s to t
	for(let i=0; i<n1; i++){
		defaultdict1[s[i]]=t[i];
	}
	// map t to s
	for(let i=0; i<n1; i++){
		defaultdict2[t[i]]=s[i];
	}
	// console.log(defaultdict1);
	// console.log(defaultdict2);
	compare1=""
	compare2=""
	for(let i=0; i<n1; i++){
		e=s[i]
		compare1+=defaultdict1[e]
	}
	for(let i=0; i<n1; i++){
		e=t[i]
		compare2+=defaultdict2[e]
	}
	if(compare1==t && compare2==s) return true
	return false
}


