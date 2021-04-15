import sys
from collections import deque

def solution(A, B):
    visited = [False for _ in range(10000)]
    queue = deque(); queue.append(('', A))
    while queue:
        command, current = queue.popleft()
        visited[current] = True

        if current == B: return command
        else :
            strA = str(current)
            if not visited[(current * 2) % 10000]:
                queue.append((command + 'D', (current * 2) % 10000))
            if not visited[(current + 9999) % 10000]:
                queue.append((command + 'S', (current + 9999) % 10000))
            if len(strA) > 1:
                if not visited[int(strA[1:] + strA[0])]:
                    queue.append((command + 'L', int(strA[1:] + strA[0])))
                if not visited[int(strA[-1] + strA[:-1])]:
                    queue.append((command + 'R', int(strA[-1] + strA[:-1])))


if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        sys.stdout.write('%s\n'%solution(A, B))