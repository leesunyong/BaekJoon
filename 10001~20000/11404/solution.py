import sys

read = sys.stdin.readline

def floyd_warshall(n, m, lines):
    graph = [[100000000] * (n + 1) for _ in range(n + 1)]
    for s, e, w in lines:
        if graph[s][e] == 0 or graph[s][e] > w:
            graph[s][e] = w
    for i in range(n + 1): graph[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]


    for g in graph[1:]:
        sys.stdout.write('%s\n'%(' '.join([str(a) if a < 100000000 else '0' for a in g[1:]])))

if __name__ == '__main__':
    n = int(read())
    m = int(read())
    lines = [list(map(int, read().split())) for _ in range(m)]

    floyd_warshall(n, m, lines)