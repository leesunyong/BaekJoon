from sys import stdin, stdout

def solution(N, K, friends):
    graph = [[7] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1): graph[i][i] = 0
    for f1, f2 in friends:
        graph[f1][f2] = graph[f2][f1] = 1
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] > 6:
                stdout.write('Big World!\n')
                return
    
    stdout.write('Small World!\n')

if __name__ == '__main__':
    N, K = map(int, stdin.readline().split())
    friends = [tuple(map(int, stdin.readline().split())) for _ in range(K)]

    solution(N, K, friends)