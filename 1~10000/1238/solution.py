import sys
import heapq

def dijkstra(start, N, graph):
    q = [(0, start)]; heapq.heappush(q, (0, start))
    weight = [sys.maxsize] * (N + 1); weight[start] = 0

    while q:
        w, current = heapq.heappop(q)

        for e, t in graph[current]:
            if weight[e] > w + t:
                weight[e] = w + t
                heapq.heappush(q, (weight[e], e))

    return weight[1:]

def solution(N, X, T):
    graphTo = [[] for _ in range(N + 1)]
    graphFrom = [[] for _ in range(N + 1)]
    for s, e, t in T:
        graphTo[s].append((e, t))
        graphFrom[e].append((s, t))

    r1 = dijkstra(X, N, graphTo)
    r2 = dijkstra(X, N, graphFrom)
    
    return max([n1 + n2 for n1, n2 in zip(r1, r2)])

if __name__ == '__main__':
    N, M, X = map(int, sys.stdin.readline().split())
    T = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    sys.stdout.write('%d\n'%(solution(N, X, T)))