import sys

def solution(neverHeard, neverSeen):
    idxH, idxS = 0, 0

    neverHeardSeen = []
    neverHeard.sort()
    neverSeen.sort()
    while idxH < len(neverHeard) and idxS < len(neverSeen):
        if neverHeard[idxH] == neverSeen[idxS]:
            neverHeardSeen.append(neverHeard[idxH])
            idxH += 1
            idxS += 1
        elif neverHeard[idxH] > neverSeen[idxS]:
            idxS += 1
        else :
            idxH += 1

    sys.stdout.write(str(len(neverHeardSeen)) + '\n')
    for n in neverHeardSeen:
        sys.stdout.write(n + '\n')

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    neverHeard, neverSeen = [], []

    for _ in range(N):
        neverHeard.append(sys.stdin.readline()[:-1])

    for _ in range(M):
        neverSeen.append(sys.stdin.readline()[:-1])

    solution(neverHeard, neverSeen)