#    Author : Mohamed Yousef 
#    Date   : 2022-12-15
import sys,math,bisect,collections,itertools,heapq
from collections import defaultdict,deque
sys.setrecursionlimit(50000) #To increase Recursion depth in py
def solve(board):
    # Check for Columns
    for i in range(9):
        added=0
        mySet=set()
        for j in range(9):
            selectedBoard=board[j][i]
            if selectedBoard not in mySet or selectedBoard==".":
                mySet.add(selectedBoard)
                added+=1
        if added!=9:
            return False
    # Check For Rows
    for i in range(9):
        added=0
        mySet=set()
        for j in range(9):
            selectedBoard=board[i][j]
            if selectedBoard not in mySet or selectedBoard==".":
                mySet.add(selectedBoard)
                added+=1
        if added!=9:
            return False
    # Check for every Three X Three square.
    for n in range(0,9,3):
        for m in range(0,9,3):
            mySet=set()
            for i in range(n,3+n):
                for j in range(m,3+m):
                    selected=board[i][j]
                    if selected in "123456789" and selected in mySet:
                        return False
                    mySet.add(selected)
    return True

print(solve(
    [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
))