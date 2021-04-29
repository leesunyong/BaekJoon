import sys
from collections import deque

def solution(N, K):
    time = [sys.maxsize] * (200001)
    current = N; time[current] = 0
    queue = deque(); queue.append((0, current))
    while queue:
        passed, location = queue.popleft()
        if location == K: 
            cnt = 1
            
            while queue:
                p, l = queue.popleft()
                if l == K and p == passed:
                    cnt += 1
                elif p > passed:
                    break

            return passed, cnt
        
        if location < K and time[location + 1] >= passed + 1:
            time[location + 1] = passed + 1
            queue.append((passed + 1, location + 1))
        if location > 0 and time[location - 1] >= passed + 1:
            time[location - 1] = passed + 1
            queue.append((passed + 1, location - 1))
        if 0 < location < K and time[location * 2] >= passed + 1:
            time[location * 2] = passed + 1
            queue.append((passed + 1, location * 2))

    return time[K], cnt

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    t, cnt = solution(N, K)
    sys.stdout.write('%d\n%d\n'%(t, cnt))