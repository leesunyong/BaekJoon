import sys

def matMult(size, matA, matB):
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = sum([matA[i][k] * matB[k][j] for k in range(size)]) % 1000

    return result

def matPower(size, mat, p):
    if p == 1:
        for i in range(size):
            for j in range(size):
                mat[i][j] %= 1000
        return mat
    elif p % 2 == 0:
        result = matPower(size, mat, p // 2)
        return matMult(size, result, result)
    else :
        result = matPower(size, mat, p // 2)
        return matMult(size, mat, matMult(size, result, result))

if __name__ == '__main__':
    N, B = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    result = matPower(N, A, B)
    for i in result:
        sys.stdout.write('%s\n'%(' '.join([str(n) for n in i])))