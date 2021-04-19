import sys

def solution(table, N, ms):
    sumTable = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            sumTable[i][j] = table[i - 1][j - 1] + sumTable[i][j-1] + sumTable[i-1][j] - sumTable[i-1][j-1]

    for m in ms:
        x1, y1, x2, y2 = m
        sys.stdout.write('%d\n'%(sumTable[x2][y2] - sumTable[x1-1][y2] - sumTable[x2][y1-1] + sumTable[x1-1][y1-1]))

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    ms = []
    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        ms.append((x1, y1, x2, y2))
    
    solution(table, N, ms)