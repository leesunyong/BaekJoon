import sys

def dfs(result, prev, visited, N, M):
    if M == 1:
        for i in range(prev, N + 1):
            result.append(visited + '%d '%i)
    else :
        for i in range(prev, N + 1):
            dfs(result, i, visited + '%d '%i, N, M - 1)


def solution(N, M):
    # Combination
    result = []

    dfs(result, 1, '', N, M)

    for r in result:
        sys.stdout.write(r + '\n')
    
if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    solution(N, M)