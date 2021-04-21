import sys
import copy

sys.setrecursionlimit(10 ** 6)

def matMult(size, matA, matB):
    for i in range(size):
        s = [0 for _ in range(size)]
        for j in range(size):
            for k in range(size):
                s[j] += matA[i][k] * matB[k][j]
            if s[j] > 1000: s[j] %= 1000

        matA[i] = s


def matPower(size, mat, p):

    if p == 2:
        result = copy.deepcopy(mat)
        matMult(size, result, mat)
    elif p == 3:
        result = copy.deepcopy(mat)
        matMult(size, result, mat)
        matMult(size, result, mat)
    elif p % 2 == 0:
        result = matPower(size, mat, p // 2)
        resultCopy = copy.deepcopy(result)
        matMult(size, result, resultCopy)
    else :
        result = matPower(size, mat, p // 2)
        resultCopy = copy.deepcopy(result)
        matMult(size, result, resultCopy)
        matMult(size, result, mat)

    return result

if __name__ == '__main__':
    N, B = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = matPower(N, A, B)
    for i in result:
        sys.stdout.write('%s\n'%(' '.join([str(n) for n in i])))