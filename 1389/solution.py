import sys
from collections import deque

def solution(N, M, connection):
    answer = [sys.maxsize for _ in range(N + 1)]
    con = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        visited = [0 for _ in range(N + 1)]; visited[i] = 1
        queue = deque()
        for c in connection[i]:
            queue.append((1, c))
            con[i][c] = 1
            visited[c] = 1

        while queue:
            step, c = queue.popleft()

            for n in connection[c]:
                if i != n and con[i][n] == 0:
                    queue.append((step + 1, n))
                    con[i][n] = step + 1
                    visited[n] = 1


    minValue = sys.maxsize; minIdx = N
    for i in range(N, 0, -1):
        s = sum(con[i])
        if s <= minValue:
            minValue = s; minIdx = i

    return minIdx

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    connection = {}
    for i in range(1, N + 1): connection[i] = []

    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        connection[x].append(y); connection[y].append(x)

    sys.stdout.write('%d\n'%solution(N, M, connection))