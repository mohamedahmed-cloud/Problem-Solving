/*
    Author : Mohamed Yousef 
    Date   : 2022-12-15
*/
let solve=function(board){
    // check for columns
    for(let i=0;i<9;i++){
        let mySet=new Set();
        let added=0 
        for(let j=0;j<9;j++){
            let selected=board[j][i];
            if( mySet.has(selected)==false || selected=="."){
                added+=1
                mySet.add(selected)
            }
        }
        if (added!=9){
            return false
        }
    }
    // Check for Rows.
    for(let i=0;i<9;i++){
        let mySet=new Set();
        let added=0 
        for(let j=0;j<9;j++){
            let selected=board[i][j];
            if( mySet.has(selected)==false || selected=="."){
                added+=1
                mySet.add(selected)
            }
        }
        if (added!=9){
            return false
        }
    }
    // Check for each 3 X 3 square Cells
    for(let n=0;n<9;n+=3){
        for(let m=0;m<9;m+=3){
            let mySet=new Set()
            for(let i=n;i<3+n;i++){
                for(let j=m;j<3+m;j++){
                    selected=board[i][j]
                    if ("123456789".includes(selected) && mySet.has(selected)==true){
                        return false
                    }
                    mySet.add(selected)
                }
            }
        }
    }   
    return true

}
console.log(solve(
    [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
));