import sys

def solution(N, M, graph):
    connected = [i for i in range(N + 1)]
    
    for g in graph:
        u, v = g
        if connected[u] != connected[v]:
            group = connected[v]
            for j, c in enumerate(connected):
                if c == group:
                    connected[j] = connected[u]

    return len(set(connected[1:]))

if __name__=='__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    graph = [[int(n) for n in sys.stdin.readline().split(' ')] for _ in range(M)]

    sys.stdout.write('%d\n'%solution(N, M, graph))