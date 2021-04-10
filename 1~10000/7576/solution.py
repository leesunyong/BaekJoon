def solution(M, N, tomatoes):
    queue = []
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i, j))

    days = 0
    while queue:
        newQueue = []
        while queue:
            x, y = queue.pop()

            if x != 0 and tomatoes[x - 1][y] == 0:
                tomatoes[x - 1][y] = 1
                newQueue.append((x - 1, y))
            if x != N - 1 and tomatoes[x + 1][y] == 0:
                tomatoes[x + 1][y] = 1
                newQueue.append((x + 1, y))
            if y != 0 and tomatoes[x][y - 1] == 0:
                tomatoes[x][y - 1] = 1
                newQueue.append((x, y - 1))
            if y != M - 1 and tomatoes[x][y + 1] == 0:
                tomatoes[x][y + 1] = 1
                newQueue.append((x, y + 1))
            
        queue = newQueue
        days += 1

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                return -1

    return days - 1

if __name__ == '__main__':
    M, N = [int(num) for num in input().split(' ')]
    tomatoes = []
    for _ in range(N):
        tomatoes.append([int(n) for n in input().split(' ')])

    print(solution(M, N, tomatoes))