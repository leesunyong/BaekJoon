import sys
import string

def solution(m):
    a = string.ascii_uppercase + string.ascii_lowercase
    g = [[3600] * 52 for _ in range(52)]
    for i in range(52): g[i][i] = 0
    for x, y in m:
        g[a.index(x)][a.index(y)] = 1

    for i in range(52):
        for j in range(52):
            for k in range(52):
                if g[j][k] > g[j][i] + g[i][k]:
                    g[j][k] = g[j][i] + g[i][k]
                    

    for i in range(52): g[i][i] = 0
    answer = []
    for i in range(52):
        for j in range(52):
            if 0 < g[i][j] < 3600:
                answer.append('%s => %s\n'%(a[i], a[j]))

    sys.stdout.write('%d\n'%len(answer))
    for a in answer:
        sys.stdout.write(a)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    m = []
    for _ in range(N):
        a, _, b, *_ = sys.stdin.readline().split()
        m.append((a, b))

    solution(m)