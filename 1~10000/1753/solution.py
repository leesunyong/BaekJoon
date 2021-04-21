import sys
import heapq

def solution(V, K, edges):
    graph = [[] for _ in range(V + 1)]
    for u, v, w in edges:
        graph[u].append([w, v])
    
    weight = [-1 for _ in range(V + 1)]; weight[K] = 0
    queue = []
    heapq.heappush(queue, (weight[K], K))

    while queue:
        current = heapq.heappop(queue)
        
        for w, i in graph[current[1]]:
            if weight[i] == -1 or current[0] + w < weight[i]:
                weight[i] = current[0] + w
                heapq.heappush(queue, (weight[i], i))

    for w in weight[1:]:
        if w == -1: sys.stdout.write('INF\n')
        else : sys.stdout.write('%d\n'%w)

if __name__ == '__main__':
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

    solution(V, K, edges)