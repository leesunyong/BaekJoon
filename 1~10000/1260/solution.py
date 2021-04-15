import sys

def dfs(N, edge, V):
    visited = [False for _ in range(N + 1)]
    visited[V] = True
    stack = [V]
    order = [V]
    while len(stack):
        current = stack[-1]

        check = False
        for e in edge:
            if e[0] == current and not visited[e[1]]:
                stack.append(e[1])
                order.append(stack[-1])
                visited[e[1]] = True
                check = True
                break
            elif e[1] == current and not visited[e[0]]:
                stack.append(e[0])
                order.append(stack[-1])
                visited[e[0]] = True
                check = True
                break

        if not check:
            del stack[-1]

    return order

def bfs(N, edge, V):
    visited = [False for _ in range(N + 1)]
    visited[V] = True
    queue = [V]
    order = []
    while len(queue):
        current = queue[0]
        del queue[0]
        order.append(current)

        for e in edge:
            if e[0] == current and not visited[e[1]]:
                queue.append(e[1])
                visited[e[1]] = True
            elif e[1] == current and not visited[e[0]]:
                queue.append(e[0])
                visited[e[0]] = True

    return order

def solution(N, edge, V):

    dfsOrder = dfs(N, edge, V)
    bfsOrder = bfs(N, edge, V)

    sys.stdout.write(' '.join([str(n) for n in dfsOrder]) + '\n')
    sys.stdout.write(' '.join([str(n) for n in bfsOrder]) + '\n')
    
if __name__ == '__main__':
    N, M, V = [int(n) for n in sys.stdin.readline().split(' ')]
    edge = []
    for _ in range(M):
        edge.append([int(n) for n in sys.stdin.readline().split(' ')])
        if edge[-1][0] > edge[-1][1]:
            edge[-1][0], edge[-1][1] = edge[-1][1], edge[-1][0]

    edge.sort(key=lambda e : (e[0], e[1]))
    solution(N, edge, V)