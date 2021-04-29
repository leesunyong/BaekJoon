import sys

def solution(N, friends):
    graph = [[2500] * N for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
        for j in range(N):
            if friends[i][j] == 'Y': graph[i][j] = 1

    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]

    answer = [0 for _ in range(N)]; m = 0
    for i in range(N):
        for j in range(N):
            if 0 < graph[i][j] <= 2: answer[i] += 1
        
        if m < answer[i]: m = answer[i]
    
    return m

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    friends = [list(sys.stdin.readline()) for _ in range(N)]

    sys.stdout.write('%d\n'%solution(N, friends))