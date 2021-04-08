def solution(N, M, board):
    cnt = [[0 for _ in range(M - 7)] for _ in range(N - 7)]
    for i in range(N - 7):
        for j in range(M - 7):
            cntBlack, cntWhite = 0, 0
            for k in range(8):
                for l in range(8):
                    if (k + l) % 2 == 0:
                        if board[i+k][j+l] == 'B': cntBlack += 1
                        else : cntWhite += 1
                    else :
                        if board[i+k][j+l] == 'W': cntBlack += 1
                        else : cntWhite += 1
            cnt[i][j] = min(cntBlack, cntWhite)
    
    minValue = 64
    for c in cnt:
        for m in c:
            if m < minValue:
                minValue = m
    
    return minValue

if __name__ == '__main__':
    N, M = [int(n) for n in input().split(' ')]
    board = []
    for _ in range(N):
        board.append(list(input()))

    print(solution(N, M, board))