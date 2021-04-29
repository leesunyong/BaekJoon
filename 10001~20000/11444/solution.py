import sys

def solution(N, f):
    if N == 0: return 0
    elif N == 1 or N == 2: return 1
    elif N == 3: return 2
    else :
        if N % 2 == 1:
            if not (N + 1) // 2 in f: f[(N + 1) // 2] = solution((N + 1) // 2, f)
            if not (N - 1) // 2 in f: f[(N - 1) // 2] = solution((N - 1) // 2, f)

            f1 = f[(N + 1) // 2]
            f2 = f[(N - 1) // 2]

            return (f1 * f1 + f2 * f2) % 1_000_000_007
        else :
            if not N // 2 in f: f[N // 2] = solution(N // 2, f)
            if not N // 2 - 1 in f: f[N // 2 - 1] = solution(N // 2 - 1, f)

            f1 = f[N // 2]
            f2 = f[N // 2 - 1]

            return (f1 * (f1 + 2 * f2)) % 1_000_000_007


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    f = {}; f[0] = 0; f[1] = 1; f[2] = 1; f[3] = 2
    sys.stdout.write('%d\n'%solution(N, f))