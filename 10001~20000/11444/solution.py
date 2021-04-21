import sys

def solution(N):
    if N == 0: return 0
    elif N == 1: return 1
    elif N == 2: return 1

    if N % 2 == 1:
        fNplusOne = solution((N + 1) // 2)
        fN = solution((N - 1) // 2)
        return (fNplusOne ** 2 + fN ** 2) % 1000000007
    else :
        a = N // 2
        fN = solution(a)
        fNminuOne = solution(a - 1)
        return (fN * (fNminuOne * 2 + fN)) % 1000000007
if __name__ == '__main__':
    N = int(sys.stdin.readline())
    sys.stdout.write('%d\n'%solution(N))