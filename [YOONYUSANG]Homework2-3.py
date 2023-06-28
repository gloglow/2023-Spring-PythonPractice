def check(n):
    for i in range(9):
        if n.count(i+1)>1:
            return False
    return True

board = [[5,3,0,0,7,0,0,0,0]
,[6,0,0,1,9,5,0,0,0]
,[0,9,8,0,0,0,0,6,0]
,[8,0,0,0,6,0,0,0,3]
,[4,0,0,8,0,3,0,0,1]
,[7,0,0,0,2,0,0,0,6]
,[0,6,0,0,0,0,2,8,0]
,[0,0,0,4,1,9,0,0,5]
,[0,0,0,0,8,0,0,7,9]]

tmp_board = []

for i in range(9):
    if check(board[i])==False:
        print('Invalid')
        quit()

for i in range(9):
    for j in range(9):
        tmp_board.append(board[j][i])
    if check(tmp_board)==False:
        print('Invalid')
        quit()
    tmp_board=[]

for i in [0,3,6]:
    for j in [0,3,6]:
        for k in range(3):
            tmp_board.append(board[i][j+k])
            tmp_board.append(board[i+1][j+k])
            tmp_board.append(board[i+2][j+k])
        if check(tmp_board)==False:
            print('Invalid')
            quit()
        tmp_board=[]

print('Valid')
