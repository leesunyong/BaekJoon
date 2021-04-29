import sys

def solution(N, K, stuff):
    arr = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(K + 1):
            arr[i][j] = arr[i - 1][j]
            if stuff[i - 1][0] <= j:
                arr[i][j] = max(arr[i][j], stuff[i - 1][1] + arr[i - 1][j - stuff[i - 1][0]])

    return arr[N][K]

if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    stuff = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    sys.stdout.write('%d\n'%solution(N, K, stuff))