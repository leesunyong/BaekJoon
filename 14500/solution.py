import sys

def bfs(numbers, visited, current, depth):

    visited[current[0]][current[1]] = True
    depth += 1
    value = 0
    if current[0] > 0 and not visited[current[0] - 1][current[1]] and depth < 4:
        tmp = bfs(numbers, visited, (current[0]-1, current[1]), depth + 1) + numbers[current[0] - 1][current[1]]
        if tmp > value: value = tmp

    return value

def solution(N, M, numbers):
    maxSum = 0

    for i in range(N):
        for j in range(M):
            value = numbers[i][j]
            visited = [[False for _ in range(M)] for _ in range(N)]
            tmp = bfs(numbers, visited, (i, j), 1) + value

            if tmp > maxSum: 
                print(i, j, tmp)
                maxSum = tmp

    return maxSum

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    numbers = []
    for _ in range(N):
        numbers.append([int(n) for n in sys.stdin.readline().split(' ')])

    print(solution(N, M, numbers))