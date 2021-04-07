def solution(N, M, maze):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1

    queue = [(0, 0)]
    while queue:
        i, j = queue[0]
        del queue[0]

        maze[i][j] = '0'

        if i != 0 and maze[i - 1][j] == '1':
            if visited[i - 1][j] == 0 or visited[i - 1][j] > visited[i][j] + 1:
                queue.append((i - 1, j))
                visited[i - 1][j] = visited[i][j] + 1
        if j != 0 and maze[i][j - 1] == '1':
            if visited[i][j - 1] == 0 or visited[i][j - 1] > visited[i][j] + 1:
                queue.append((i, j - 1))
                visited[i][j - 1] = visited[i][j] + 1
        if i < N - 1 and maze[i + 1][j] == '1':
            if visited[i + 1][j] == 0 or visited[i + 1][j] > visited[i][j] + 1:
                queue.append((i + 1, j))
                visited[i + 1][j] = visited[i][j] + 1
        if j < M - 1 and maze[i][j + 1] == '1':
            if visited[i][j + 1] == 0 or visited[i][j + 1] > visited[i][j] + 1:
                queue.append((i, j + 1))
                visited[i][j + 1] = visited[i][j] + 1

    return visited[N-1][M-1]

if __name__ == '__main__':
    N, M = [int(n) for n in input().split(' ')]
    maze = []
    for _ in range(N):
        line = input()
        maze.append(list(line))

    print(solution(N, M, maze))