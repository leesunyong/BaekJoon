import sys

def solution(N):
    cnt = 0
    for i in range(1, N + 1):
        tmp = i
        while tmp % 5 == 0:
            cnt += 1
            tmp //= 5
            if tmp == 0: break

    return cnt

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sys.stdout.write(str(solution(N)) + '\n')