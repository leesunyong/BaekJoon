import sys
from collections import deque

def solution(T, testCase):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for t in testCase:
        M, N, K = t[0]
        cabage = t[1]
        field = [[0] * N for _ in range(M)]
        for c in cabage:
            field[c[0]][c[1]] = 1

        group = 0
        for i in range(M):
            for j in range(N):
                if field[i][j] != 0:
                    field[i][j] = 0
                    queue = deque()
                    queue.append((i, j))
                    group += 1
                    while len(queue):
                        x, y = queue.popleft()

                        for k in range(4):
                            xMove, yMove = x + dx[k], y + dy[k]
                            if 0 <= xMove < M and 0 <= yMove < N and field[xMove][yMove] == 1:
                                queue.append((xMove, yMove))
                                field[xMove][yMove] = 0

        sys.stdout.write('%d\n'%group)
    

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    testCase = []

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        cabage = [[int(n) for n in sys.stdin.readline().split()] for _ in range(K)]
        testCase.append([[M, N, K], cabage])

    solution(T, testCase)