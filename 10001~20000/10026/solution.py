import sys
from collections import deque

def bfs(start, N, picture, visited):
    mark = picture[start[0]][start[1]]
    queue = deque(); queue.append(start)
    visited[start[0]][start[1]] = True
    dx = [0, 0, 1, -1]; dy = [1, -1, 0, 0]

    while queue:
        current = queue.popleft()

        for i in range(4):
            nextX = current[0] + dx[i]; nextY = current[1] + dy[i]
            if 0 <= nextX < N and 0 <= nextY < N and not visited[nextX][nextY] and picture[nextX][nextY] == mark:
                visited[nextX][nextY] = True
                queue.append((nextX, nextY))

def solution(N, picture):
    pictureCB = [[c for c in p] for p in picture]
    for i, p in enumerate(pictureCB):
        for j, c in enumerate(p):
            if c == 'G': pictureCB[i][j] = 'R'
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    visitedCB = [[False for _ in range(N)] for _ in range(N)]

    cnt = 0; cntCB = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs((i, j), N, picture, visited)
                cnt += 1
            if not visitedCB[i][j]:
                bfs((i, j), N, pictureCB, visitedCB)
                cntCB += 1
    
    sys.stdout.write('%d %d\n'%(cnt, cntCB))

    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    picture = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
    solution(N, picture)