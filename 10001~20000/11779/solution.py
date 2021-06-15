import sys
import heapq

def solution(n, start, dest, graph):
    # Dijkstra
    q = [(0, start)]

    distance = [sys.maxsize for _ in range(n + 1)]
    distance[start] = 0

    route = [[] for _ in range(n + 1)]
    route[start] = [start]

    while q:
        cost, current = heapq.heappop(q)

        if current == dest:
            print(cost)
            print(len(route[current]))
            print(' '.join(map(str, route[current])))

            return

        for e in graph[current]:
            if distance[e[0]] > e[1] + cost:
                distance[e[0]] = e[1] + cost
                heapq.heappush(q, (e[1] + cost, e[0]))
                route[e[0]] = route[current] + [e[0]]
        

if __name__ == '__main__':
    n = int(input())
    m = int(input())

    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        
        if a in graph:
            graph[a].append((b, c))

    s, d = map(int, input().split())

    solution(n, s, d, graph)