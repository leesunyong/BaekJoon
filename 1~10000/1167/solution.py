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

def solution(V, tree):
    distance = [-1 for _ in range(V + 1)]
    distance[1] = 0

    bfs(1, tree, distance)

    maxIdx, maxDis = -1, 0
    for i in range(2, V + 1):
        if distance[i] > maxDis:
            maxIdx = i; maxDis = distance[i]

    distance = [-1 for _ in range(V + 1)]
    distance[maxIdx] = 0
    bfs(maxIdx, tree, distance)

    return max(distance)

if __name__ == '__main__':
    V = int(stdin.readline())
    tree = {}
    for _ in range(V):
        v = list(map(int, stdin.readline().split()[:-1]))
        s = v[0]; v= v[1:]
        tree[s] = [(v[i * 2], v[i * 2 + 1]) for i in range(len(v) // 2)]
    
    stdout.write('%d\n'%solution(V, tree))

# 4
# 1 2 5 3 9 -1
# 2 1 5 -1
# 3 1 9 4 8 -1
# 4 3 8 -1
# 답 : 22

# 6
# 1 2 3 -1
# 2 1 3 5 3 3 5 -1
# 3 2 5 4 7 -1
# 4 3 7 -1
# 5 2 3 6 5 -1
# 6 5 5 -1
# 답 : 20

# 4
# 1 2 7 3 2 -1
# 2 1 7 -1
# 3 1 2 4 3 -1
# 4 3 3 -1
# 답 : 12

# 5
# 1 2 7 3 2 5 10 -1
# 2 1 7 -1
# 3 1 2 4 3 -1
# 4 3 3 -1
# 5 1 10 -1
# 답 : 17