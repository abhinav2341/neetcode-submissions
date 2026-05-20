class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxCenters=[
            (1,1),(1,4),(1,7),
            (4,1),(4,4),(4,7),
            (7,1),(7,4),(7,7)
            ]
    
        for i in range(0,9):
            row=[0]*10
            col=[0]*10
            
            for j in range(0,9):
                # row check
                if board[i][j] != '.':
                    if row[int(board[i][j])] == 1:
                        return False
                    else:
                        row[int(board[i][j])] = 1
                
                # col check
                if board[j][i] != '.':
                    if col[int(board[j][i])] == 1:
                        return False
                    else:
                        col[int(board[j][i])] = 1
                
            
            for cord in boxCenters:
                box=[0]*10
                i=cord[0]
                j=cord[1]
                
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]-1
                j=cord[1]
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]+1
                j=cord[1]
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]
                j=cord[1]-1
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]
                j=cord[1]+1
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]-1
                j=cord[1]-1
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                        
                i=cord[0]+1
                j=cord[1]+1
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]+1
                j=cord[1]-1
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1
                
                i=cord[0]-1
                j=cord[1]+1
                if board[i][j] !='.':
                    if box[int(board[i][j])] == 1:
                        return False
                    else:
                        box[int(board[i][j])] = 1

        return True
        