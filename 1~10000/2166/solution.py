import sys

def solution(N, coord):
    # Shoelace Formula
    area = 0
    coord.append(coord[0])

    for i in range(N):
        area += coord[i][0] * coord[i+1][1] - coord[i][1] * coord[i+1][0]

    return abs(area) / 2

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    coord = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    sys.stdout.write('%.1f\n'%solution(N, coord))
