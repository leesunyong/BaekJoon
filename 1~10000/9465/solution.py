import sys

read = sys.stdin.readline

def solution(n, sticker):
    score = [[0] * n for _ in range(2)]
    score[0][0] = sticker[0][0]; score[1][0] = sticker[1][0]
    score[0][1] = sticker[0][1] + sticker[1][0]
    score[1][1] = sticker[1][1] + sticker[0][0]

    for i in range(2, n):
        score[0][i] = max(score[1][i-1], score[1][i-2]) + sticker[0][i]
        score[1][i] = max(score[0][i-1], score[0][i-2]) + sticker[1][i]

    return max(score[0][n - 1], score[1][n - 1])

if __name__ == '__main__':
    T = int(read())
    for _ in range(T):
        n = int(read())
        sticker = [list(map(int, read().split())) for _ in range(2)]

        sys.stdout.write('%d\n'%solution(n, sticker))