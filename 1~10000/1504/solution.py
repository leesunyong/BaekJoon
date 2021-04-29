import sys
import heapq

def dijkstra(start, N, graph):
    q = []; heapq.heappush(q, (0, start))
    weight = [sys.maxsize] * (N + 1); weight[start] = 0
    while q:
        w, current = heapq.heappop(q)

        for nc, nw in graph[current]:
            if weight[nc] > nw + w:
                weight[nc] = nw + w
                heapq.heappush(q, (weight[nc], nc))

    return weight

def solution(N, graph, v1, v2):
    g = [[] for _ in range(N + 1)]
    for s, e, w in graph:
        g[s].append((e, w)); g[e].append((s, w))

    d1 = dijkstra(v1, N, g)
    d2 = dijkstra(v2, N, g)
    a1 = d1[1] + d1[v2] + d2[N] if d1[1] != sys.maxsize and d1[v2] != sys.maxsize and d2[N] != sys.maxsize else -1
    a2 = d2[1] + d2[v1] + d1[N] if d2[1] != sys.maxsize and d2[v1] != sys.maxsize and d1[N] != sys.maxsize else -1

    return min(a1, a2)

if __name__ == '__main__':
    N, E = map(int, sys.stdin.readline().split())
    graph = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
    v1, v2 = map(int, sys.stdin.readline().split())

    sys.stdout.write('%d\n'%(solution(N, graph, v1, v2)))