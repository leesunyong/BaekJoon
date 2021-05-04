import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    maxS = [0, 0, 0]; minS = [0, 0, 0]
    for _ in range(N):
        n1, n2, n3 = map(int, sys.stdin.readline().split())
        maxS[0], maxS[1], maxS[2]\
            = n1 + max(maxS[:2]), n2 + max(maxS), n3 + max(maxS[1:])
        minS[0], minS[1], minS[2]\
            = n1 + min(minS[:2]), n2 + min(minS), n3 + min(minS[1:])

    sys.stdout.write('%d %d\n'%(max(maxS), min(minS)))