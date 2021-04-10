import sys

def solution(N, computers):
    infected = [False for _ in range(N + 1)]
    infected[1] = True

    for _ in range(N):
        for c in computers:
            if infected[c[0]] or infected[c[1]]:
                infected[c[0]] = infected[c[1]] = True

    return infected.count(True) - 1

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    computers = []
    for i in range(M):
        computers.append([int(n) for n in sys.stdin.readline().split(' ')])

    sys.stdout.write(str(solution(N, computers)) + '\n')