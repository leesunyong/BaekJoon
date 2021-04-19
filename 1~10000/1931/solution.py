import sys

def solution(N, meeting):
    meeting = sorted(meeting, key=lambda m: (m[1], m[0]))
    cnt, current = 0, 0

    for m in meeting:
        if m[0] >= current:
            cnt += 1; current = m[1]
    
    return cnt

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    meeting = [[int(n) for n in sys.stdin.readline().split(' ')] for _ in range(N)]

    sys.stdout.write('%d\n'%solution(N, meeting))