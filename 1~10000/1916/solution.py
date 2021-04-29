import sys
import heapq

read = sys.stdin.readline

def solution(N, M, buses, start, end):
    cities = [[] for _ in range(N + 1)]
    for s, e, w in buses:
        cities[s].append((e, w))

    weight = [sys.maxsize for _ in range(N + 1)]; weight[start] = 0

    queue = []; heapq.heappush(queue, (weight[start], start))

    while queue:
        w, dest = heapq.heappop(queue)

        if dest == end: break

        for e, w1 in cities[dest]:
            if weight[e] > w + w1:
                weight[e] = w + w1
                heapq.heappush(queue, (weight[e], e))
        
    return weight[end]

if __name__ == '__main__':
    N = int(read())
    M = int(read())
    buses = [list(map(int, read().split())) for _ in range(M)]
    start, end = map(int, read().split())

    sys.stdout.write('%d\n'%solution(N, M, buses, start, end))