# Very bad problem.

from typing import Optional, List

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        O = 0
        X = 0
        isOver1 = 0
        isOver2 = 0
        for i in board:
            isOver1 += 1 if i.count("O") == 3 else 0
            isOver2 += 1 if i.count("X") == 3 else 0
            O += i.count("O")
            X += i.count("X")

        if isOver1 > 1 or isOver2 > 1:
            print("From Here 1")
            return False
        x = [isOver1, isOver2]
        def over(board):
            nonlocal isOver1, isOver2
            for i in range(3):
                prev = 0
                equal = 0 
                for j in range(3):
                    if  (not prev or prev == board[j][i]) and board[j][i] != " ":
                        prev = board[j][i]
                        equal += 1
                
                if equal == 3 and prev == "O": 
                    isOver1 += 1
                if equal == 3 and prev == "X": 
                    isOver2 += 1
                    
        over(board)

        if isOver1 - x[0] > 1 or isOver2 - x[1] > 1: 
            print("From Here 2")
            return False
        x = [isOver1, isOver2]

        def overOver(board):
            nonlocal isOver1, isOver2
            prev1 = 0
            equal1 = 0
            equal2 = 0
            prev2 = 0
            for i in range(3):
                for j in range(3):
                    
                    if i == j and (not prev1 or prev1 == board[i][j]) and board[i][j] != " ":
                        equal1 += 1
                        prev1 = board[i][j]

                    if i + j == 2 and (not prev2 or prev2 == board[i][j]) and board[i][j] != " " :
                        equal2 += 1
                        prev2 = board[i][j]
            
            if equal1 == 3 :
                if prev1 == "O": isOver1 += 1
                else: isOver2 += 1
            # print(equal2, prev2, equal1, prev1)
            if equal2 == 3 :
                if prev2 == "O": isOver1 += 1
                else: isOver2 += 1


        overOver(board)
        # print(isOver1)

        if isOver1 - x[0] > 2 or isOver2 - x[1] > 2: 
            # print("From here 3")
            return False

        print(isOver1, isOver2, X, O)
        if isOver2 and O == X: return False
        if isOver1 and O < X: return False
        if isOver1 and isOver2: return False
        if isOver2 and X == O : return False

        if isOver1 > 2: return False
        if isOver2  > 2: return False
        # print("here")
        if X - O  in [0, 1]: 
            # print("hereda")
            return True
        
        return False

slv = Solution()
# print(slv.validTicTacToe(["OXX","XOX","OXO"]))
# print(slv.validTicTacToe(["XOX","OXO","XOX"]))
print(slv.validTicTacToe(["XOX","OXO","XOX"]))