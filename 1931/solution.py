import sys

def solution(N, meeting):
    meeting = sorted(meeting, key=lambda m: (m[0], m[1]), reverse=True)
    cnt = [0 for _ in range(N)]
    cnt[0] = 1

    
    print(meeting)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    meeting = [[int(n) for n in sys.stdin.readline().split(' ')] for _ in range(N)]

    sys.stdout.write('%d\n'%solution(N, meeting))