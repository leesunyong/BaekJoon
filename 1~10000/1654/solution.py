import sys

def solution(K, N, cables):
    maxLength = max(cables)

    right, left = maxLength, 1
    answer = 0
    while True:
        cnt = 0
        current = (right + left) // 2

        for c in cables:
            cnt += c // current

        if cnt < N:
            right = current - 1
        elif cnt >= N:
            answer = current
            left = current + 1

        if right < left: return answer

if __name__ == '__main__':
    K, N = [int(n) for n in sys.stdin.readline().split(' ')]
    cables = []
    for i in range(K):
        cables.append(int(sys.stdin.readline()))

    sys.stdout.write(str(solution(K, N, cables)) + '\n')