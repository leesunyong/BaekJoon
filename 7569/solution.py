def solution(M, N, H, tomatoes):
    queue = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 1:
                    queue.append((i, j, k))

    days = 0
    while queue:
        newQueue = []
        while queue:
            x, y, z = queue.pop()

            if x != 0 and tomatoes[x - 1][y][z] == 0:
                tomatoes[x - 1][y][z] = 1
                newQueue.append((x - 1, y, z))
            if x != H - 1 and tomatoes[x + 1][y][z] == 0:
                tomatoes[x + 1][y][z] = 1
                newQueue.append((x + 1, y, z))
            if y != 0 and tomatoes[x][y - 1][z] == 0:
                tomatoes[x][y - 1][z] = 1
                newQueue.append((x, y - 1, z))
            if y != N - 1 and tomatoes[x][y + 1][z] == 0:
                tomatoes[x][y + 1][z] = 1
                newQueue.append((x, y + 1, z))
            if z != 0 and tomatoes[x][y][z - 1] == 0:
                tomatoes[x][y][z - 1] = 1
                newQueue.append((x, y, z - 1))
            if z != M - 1 and tomatoes[x][y][z + 1] == 0:
                tomatoes[x][y][z + 1] = 1
                newQueue.append((x, y, z + 1))
            
        queue = newQueue
        days += 1

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 0:
                    return -1

    return days - 1

if __name__ == '__main__':
    M, N, H = [int(num) for num in input().split(' ')]
    tomatoes = [[[int(n) for n in input().split(' ')] for _ in range(N)] for _ in range(H)]

    print(solution(M, N, H, tomatoes))