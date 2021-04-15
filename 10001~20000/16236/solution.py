import sys
from collections import deque
import copy

def bfs(start, size, N, aquarium):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = True

    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    distance = 0
    queue = [start]; target = []
    while queue:
        for q in queue:
            if 0 < aquarium[q[0]][q[1]] < size:
                target.append(q)
        
        if len(target):
            target = sorted(target, key=lambda f: (f[0], f[1]))
            return (distance, target[0])

        newQueue = []
        for q in queue:
            for i in range(4):
                nextX = q[0] + dx[i]; nextY = q[1] + dy[i]
                if 0 <= nextX < N and 0 <= nextY < N:
                    if aquarium[nextX][nextY] <= size and not visited[nextX][nextY]:
                        newQueue.append((nextX, nextY))
                        visited[nextX][nextY] = True

        queue = newQueue
        distance += 1

    return None

def solution(N, aquarium):

    # find current location
    current = None
    for i in range(N):
        for j in range(N):
            if aquarium[i][j] == 9:
                current = (i, j)
                break
        if not (current is None) : break
                
    size = 2; cnt = 0
    time = 0

    while True:
        aquarium[current[0]][current[1]] = 0

        # find target fish
        # if there is no fish, return time
        targetFish = bfs(current, size, N, aquarium)
        if targetFish is None: return time

        distance, current = targetFish
        time += distance

        cnt += 1
        if cnt == size: cnt = 0; size += 1

    

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    aquarium = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    sys.stdout.write('%d\n'%solution(N, aquarium))