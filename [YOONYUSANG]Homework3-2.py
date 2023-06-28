def sup_valid_move(n): 
    if n%3==0:
        return [n+1, n+2]
    elif n%3==1:
        return [n-1, n+1]
    else:
        return [n-2, n-1]

def valid_move(board, row, column, number):
    if board[row].count(number)>0:
        return False
    for _ in range(0,9):
        if board[_][column]==number:
            return False
    for i in sup_valid_move(row):
        for j in sup_valid_move(column):
            if board[i][j]==number:
                return False
    return True

def solve_sudoku(board):
    i=0
    j=0
    k=0
    save_i=0
    save_j=0
    save_k=1
    not_found=0
    save_point=[]
    while i<9:
        if j>8:
            j=0
        else:
            j=save_j
        while j<9:
            if board[i][j]!=0:
                j=j+1
                continue
            else:
                k=save_k
                while k<10:
                    if valid_move(board, i, j, k)==True:
                        board[i][j]=k
                        save_point.append([i,j])
                        save_k=1
                        not_found=0
                        break
                    not_found=1
                    k=k+1
                if not_found==1:
                    if(len(save_point)==0):
                        return 'There is not solution'
                    save_i,save_j=save_point[-1]
                    save_k=board[save_i][save_j]+1
                    board[save_i][save_j]=0
                    i=save_i
                    save_point.pop()
                    break
            j=j+1
        if not_found==0:
            i=i+1
    return board        

    
board=[]