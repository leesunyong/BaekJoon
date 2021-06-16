import sys
from collections import deque

def solution(N):
    parent = [None] * (N + 1)
    count = [sys.maxsize] * (N + 1)
    count[N] = 0

    q = deque(); q.append(N)

    while q:
        current = q.popleft()
        if current % 3 == 0:
            next = current // 3
            if count[next] > count[current] + 1:
                count[next] = count[current] + 1
                parent[next] = current
                if next == 1: break
                q.append(next)

        if current % 2 == 0:
            next = current // 2
            if count[next] > count[current] + 1:
                count[next] = count[current] + 1
                parent[next] = current
                if next == 1: break
                q.append(next)

        next = current - 1
        if count[next] > count[current] + 1:
            count[next] = count[current] + 1
            parent[next] = current
            if next == 1: break
            q.append(next)

    current = 1
    print(count[current])
    
    path = []
    while current:
        path.append(str(current))
        current = parent[current]
    path.reverse()
    print(' '.join(path))

if __name__ == '__main__':
    N = int(input())

    solution(N)