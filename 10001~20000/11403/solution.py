import sys

def solution(N, graph):

    for _ in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] != 1:
                    for k in range(N):
                        if graph[i][k] == 1 and graph[k][j] == 1:
                            graph[i][j] = 1
                            break

    for g in graph:
        sys.stdout.write('%s\n'%(' '.join([str(c) for c in g])))

if __name__=='__main__':
    N = int(sys.stdin.readline())
    graph = [[int(n) for n in sys.stdin.readline().split(' ')[:N]] for _ in range(N)]

    solution(N, graph)