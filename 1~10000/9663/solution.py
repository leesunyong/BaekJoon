import sys

def nQueen(row, di1, di2, i, N):
    answer = 0

    for c in range(N):
        if row[c] != 1 and di1[i - c + N] != 1 and di2[i + c] != 1:
            if i + 1 == N: answer += 1
            else :
                row[c] = 1; di1[i - c + N] = 1; di2[i + c] = 1
                answer += nQueen(row, di1, di2, i + 1, N)
                row[c] = 0; di1[i - c + N] = 0; di2[i + c] = 0

    return answer

def solution(N):
    row = [0 for _ in range(N)]
    di1 = [0 for _ in range(2 * N)]
    di2 = [0 for _ in range(2 * N)]

    answer = 0
    for c in range(N // 2):
        if row[c] != 1 and di1[N - c] != 1 and di2[c] != 1:
            if N == 1: answer += 1
            else :
                row[c] = 1; di1[N - c] = 1; di2[c] = 1
                answer += nQueen(row, di1, di2, 1, N)
                row[c] = 0; di1[N - c] = 0; di2[c] = 0
    answer *= 2

    if N % 2 == 1:
        c = N // 2
        if row[c] != 1 and di1[N - c] != 1 and di2[c] != 1:
            if N == 1: answer += 1
            else :
                row[c] = 1; di1[N - c] = 1; di2[c] = 1
                answer += nQueen(row, di1, di2, 1, N)
                row[c] = 0; di1[N - c] = 0; di2[c] = 0

    return answer

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    sys.stdout.write('%d\n'%solution(N))