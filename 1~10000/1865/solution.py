import sys
import heapq

def solution(N, graph):
    queue = [(0, i, i) for i in range(1, N + 1)]

    while queue:
        print(queue)
        w, s, e = heapq.heappop(queue)

        if w < 0: return 'YES'

        for i, g in enumerate(graph[e]):
            if g != 0 and (graph[s][i] == 0 or graph[s][i] > g + w):
                graph[s][i] = g + w
                heapq.heappush(queue, (w + g, s, i))
    
    return 'NO'

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M, W = map(int, sys.stdin.readline().split())
        g = [[0] * (N + 1) for _ in range(N + 1)]
        for _ in range(M):
            s, e, w = map(int, sys.stdin.readline().split())
            if g[s][e] == 0 or g[s][e] > w: g[s][e] = w
        
        for _ in range(W):
            s, e, w = map(int, sys.stdin.readline().split())
            if g[s][e] == 0 or g[s][e] > w: g[s][e] = -w
        
        sys.stdout.write('%s\n'%solution(N, g))
            