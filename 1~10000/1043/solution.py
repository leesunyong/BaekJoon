from sys import stdin, stdout

def solution(N, M, nT, T, P):
    truth = [False for _ in range(N + 1)]
    answer = [False for _ in range(M)]
    for t in T:
        truth[t] = True

        for i, p in enumerate(P):
            if not answer[i] and t in p[1:]:
                for g in p[1:]:
                    if not truth[g]:
                        truth[g] = True
                        T.append(g)
                answer[i] = True

    return answer.count(False)

if __name__ == '__main__':
    N, M = map(int, stdin.readline().split())
    T = list(map(int, stdin.readline().split()))
    nT, T = T[0], T[1:]
    P = [list(map(int, stdin.readline().split())) for _ in range(M)]

    stdout.write('%d\n'%solution(N, M, nT, T, P))