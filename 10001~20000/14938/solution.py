import sys

def solution(n, m, nItem, graph):
    distance = [[sys.maxsize] * (n + 1) for _ in range(n + 1)]
    for e in graph:
        distance[e[0]][e[1]] = e[2]
        distance[e[1]][e[0]] = e[2]

    for v in range(n):
        distance[v][v] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    items = [0 for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] <= m:
                items[i] += nItem[j - 1]

    return max(items[1:])

if __name__ == '__main__':
    n, m, r = map(int, sys.stdin.readline().split())
    nItem = list(map(int, sys.stdin.readline().split()))
    
    graph = []
    for _ in range(r):
        graph.append(tuple(map(int, sys.stdin.readline().split())))

    print(solution(n, m, nItem, graph))