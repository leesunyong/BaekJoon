import sys
from collections import deque

def solution(N, M, m):
    if N == 1 and M == 1: return 1

    # coordinate, wall, distance 
    q = deque(); q.append(((0, 0), 0, 1))
    dx = [0, 0, 1, -1]; dy = [1, -1, 0, 0]
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]

    while q:
        current, wall, count = q.popleft()

        for i in range(4):
            nX = current[0] + dx[i]; nY = current[1] + dy[i]
            if nX == N - 1 and nY == M - 1: return count + 1
            
            if 0 <= nX < N and 0 <= nY < M:
                if m[nX][nY] == '0' and not visited[nX][nY][wall]:
                    visited[nX][nY][wall] = True
                    q.append(((nX, nY), wall, count + 1))
                elif wall == 0 and not visited[nX][nY][1]:
                    visited[nX][nY][1] = True
                    q.append(((nX, nY), 1, count + 1))

    return -1

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    m = [list(sys.stdin.readline()[:-1]) for _ in range(N)]
    print(solution(N, M, m))