import sys

def solution(N):
    tile = [0 for _ in range(1001)]
    tile[1] = 1
    tile[2] = 3

    for i in range(3, N + 1):
        tile[i] = (tile[i - 1] + tile[i - 2] * 2) % 10007
    
    return tile[N]

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sys.stdout.write(str(solution(N)) + '\n')