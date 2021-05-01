import sys

def solution(N, edges):
    g = [100000000 for _ in range(N + 1)]; g[0] = 0
    
    for _ in range(N):
        update = False
        for s, e, t in edges:
            if g[e] > g[s] + t:
                g[e] = g[s] + t
                update = True
        
        if not update: break

    for s, e, t in edges:
        if g[e] > g[s] + t:
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    TC = int(sys.stdin.readline())
    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split())
        edges = []
        for _ in range(M):
            s, e, w = map(int, sys.stdin.readline().split())
            edges.append((s, e, w))
            edges.append((e, s, w))
        
        for _ in range(W):
            s, e, w = map(int, sys.stdin.readline().split())
            edges.append((s, e, -w))
        
        sys.stdout.write('%s\n'%solution(N, edges))
            