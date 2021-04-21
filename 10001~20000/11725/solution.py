import sys

sys.setrecursionlimit(10 ** 6)

read = sys.stdin.readline

def bfs(parents, p, nodes):
    for n in nodes[p]:
        if parents[n] == 0:
            parents[n] = p
            bfs(parents, n, nodes)

def solution(N, nodes):
    parents = [0 for _ in range(N + 1)]
    parents[1] = 1
    
    bfs(parents, 1, nodes)

    for p in parents[2:]:
        sys.stdout.write('%d\n'%p)

if __name__ == '__main__':
    N = int(read())
    nodes = {}
    for _ in range(N - 1):
        x, y = map(int, read().split())

        if x in nodes: nodes[x].append(y)
        else : nodes[x] = [y]

        if y in nodes: nodes[y].append(x)
        else : nodes[y] = [x]   

    solution(N, nodes)