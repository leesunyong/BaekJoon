def solution(board):
    possible = [[[True] * 10 for _ in range(9)] for _ in range(9)]
    count = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                count += 1
                for k in range(10):
                    possible[i][j][k] = False
                
                for k in range(9):
                    possible[i][k][board[i][j]] = False
                    possible[k][j][board[i][j]] = False
                    possible[(i//3)*3 + k//3][(j//3)*3 + k%3][board[i][j]] = False

    while count < 81:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if possible[i][j].count(True) == 2:
                    count += 1
                    board[i][j] = possible[i][j].index(True, 1)

                    for k in range(10):
                        possible[i][j][k] = False

                    for k in range(9):
                        possible[i][k][board[i][j]] = False
                        possible[k][j][board[i][j]] = False
                        possible[(i//3)*3 + k//3][(j//3)*3 + k%3][board[i][j]] = False
    
    # for i in range(9):
    #     print('%d %d %d|%d %d %d|%d %d %d'%(board[i][0],board[i][1],board[i][2],board[i][3],board[i][4],board[i][5],board[i][6],board[i][7],board[i][8]))
    #     if (i + 1) % 3 == 0: print('-----------------')

    for i in range(9):
        print('%d%d%d%d%d%d%d%d%d'%(board[i][0],board[i][1],board[i][2],board[i][3],board[i][4],board[i][5],board[i][6],board[i][7],board[i][8]))
    

board = [list(map(int, list(input()))) for _ in range(9)]

solution(board)