def dfs(R, C, board):
    max_move = 0
    stack = [(0, 0, 1, board[0][0])]
    next_move_x = [1, -1, 0, 0]
    next_move_y = [0, 0, 1, -1]
    check = [['']*C for _ in range(R)]

    while stack:
        current_x, current_y, move, used_alphabet = stack.pop()
        
        if move > max_move: max_move = move

        if max_move == 26:
            break

        for i in range(4):
            next_x = next_move_x[i] + current_x
            next_y = next_move_y[i] + current_y

            if 0 <= next_x < R and 0 <= next_y < C:
                if board[next_x][next_y] not in used_alphabet:
                    tmp = used_alphabet + board[next_x][next_y]
                    if check[next_x][next_y] != tmp:
                        check[next_x][next_y] = tmp
                        stack.append((next_x, next_y, move + 1, tmp))

    return max_move

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
print(dfs(R, C, board))