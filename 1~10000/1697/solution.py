import sys
from collections import deque

def solution(N, K):
    time = [sys.maxsize] * (200001)
    current = N; time[current] = 0
    queue = deque(); queue.append((0, current))

    while queue:
        passed, location = queue.popleft()
        if location == K: return passed
        
        if location < K and time[location + 1] > passed + 1:
            time[location + 1] = passed + 1
            queue.append((passed + 1, location + 1))
        if location > 0 and time[location - 1] > passed + 1:
            time[location - 1] = passed + 1
            queue.append((passed + 1, location - 1))
        if 0 < location < K and time[location * 2] > passed + 1:
            time[location * 2] = passed + 1
            queue.append((passed + 1, location * 2))

    return time[K]

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    sys.stdout.write('%d\n'%solution(N, K))