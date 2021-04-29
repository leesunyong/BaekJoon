from sys import stdin, stdout
from collections import deque

def bfs(node, tree, distance):
    
    queue = deque(); queue.append(node)
    while queue:
        current = queue.popleft()

        for n, w in tree[current]:
            if distance[n] == -1:
                distance[n] = w + distance[current]

                queue.append(n)

def solution(n, tree):
    distance = [-1 for _ in range(n + 1)]
    distance[1] = 0

    bfs(1, tree, distance)


    maxIdx, maxDis = 1, 0
    for i in range(2, n + 1):
        if distance[i] > maxDis:
            maxIdx = i; maxDis = distance[i]

    distance = [-1 for _ in range(n + 1)]
    distance[maxIdx] = 0
    bfs(maxIdx, tree, distance)

    return max(distance)

if __name__ == '__main__':
    n = int(stdin.readline())
    tree = {}; tree[1] = []
    for _ in range(n - 1):
        v = list(map(int, stdin.readline().split()))

        if v[0] in tree:
            tree[v[0]].append((v[1], v[2]))
        else :
            tree[v[0]] = [(v[1], v[2])]
        
        if v[1] in tree:
            tree[v[1]].append((v[0], v[2]))
        else :
            tree[v[1]] = [(v[0], v[2])]
    
    stdout.write('%d\n'%solution(n, tree))