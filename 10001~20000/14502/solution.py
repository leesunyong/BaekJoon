from sys import stdin, stdout

def bfs(N, M, m, virus):
    visited = [[False] * M for _ in range(N)]
    
    cnt = 0
    q = [*virus]; idx = 0
    
    dx = [1, -1, 0, 0]; dy = [0, 0, 1, -1]
    while idx != len(q):
        c = q[idx]; idx += 1

        for i in range(4):
            nX = c[0] + dx[i]; nY = c[1] + dy[i]
            if 0 <= nX < N and 0 <= nY < M and not visited[nX][nY] and m[nX][nY] == 0:
                visited[nX][nY] = True
                cnt += 1
                q.append((nX, nY))
    
    return cnt

def solution(N, M, board, virus, safe):
    cnt = len(safe) - 3

    ans = 0
    for i in range(len(safe) - 2):
        board[safe[i][0]][safe[i][1]] = 1
        for j in range(i + 1, len(safe) - 1):
            board[safe[j][0]][safe[j][1]] = 1
            for k in range(j + 1, len(safe)):
                board[safe[k][0]][safe[k][1]] = 1

                tmp = cnt - bfs(N, M, board, virus)
                if tmp > ans: ans = tmp

                board[safe[k][0]][safe[k][1]] = 0
            board[safe[j][0]][safe[j][1]] = 0
        board[safe[i][0]][safe[i][1]] = 0

    return ans
    

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    board = []; virus = []; safe = []
    for i in range(N):
        board.append(list(map(int, stdin.readline().split())))
        for j in range(M):
            if board[i][j] == 2: virus.append((i, j))
            elif board[i][j] == 0: safe.append((i, j))

    stdout.write('%s\n'%solution(N, M, board, virus, safe))
