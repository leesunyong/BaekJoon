import sys

input = sys.stdin.readline

def solution(N, board):
    visit = [[[0] * N for _ in range(N)] for _ in range(3)]; visit[0][0][1] = 1
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == '0' and j > 0:
                visit[0][i][j] += visit[0][i][j-1] + visit[2][i][j-1]
            if board[i][j] == '0' and i > 0:
                visit[1][i][j] += visit[1][i-1][j] + visit[2][i-1][j]
            if board[i][j] == '0' and j > 0 and i > 0 and board[i-1][j] == '0' and board[i][j-1] == '0':
                visit[2][i][j] += visit[0][i-1][j-1] + visit[1][i-1][j-1] + visit[2][i-1][j-1]

    return visit[0][N-1][N-1] + visit[1][N-1][N-1] + visit[2][N-1][N-1]

if __name__ == '__main__':
    N = int(input())
    board = [input().split() for _ in range(N)]

    print(solution(N, board))