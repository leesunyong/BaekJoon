import sys

def spread(R, C, room):
    s = [[0] * C for _ in range(R)]
    dx = [-1, 1, 0, 0]; dy = [0, 0, -1, 1]

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                dust = room[i][j] // 5
                for k in range(4):
                    nX = i + dx[k]; nY = j + dy[k]
                    if 0 <= nX < R and 0 <= nY < C and room[nX][nY] != -1:
                        s[i][j] -= dust
                        s[nX][nY] += dust

    for i in range(R):
        for j in range(C):
            room[i][j] += s[i][j]

def purify(R, C, airP, room):
        
    for i in range(airP[0] - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for i in range(airP[1] + 1, R - 1):
        room[i][0] = room[i + 1][0]

    room[0] = room[0][1:] + [0]
    room[R - 1] = room[R - 1][1:] + [0]
    
    for i in range(airP[0]):
        room[i][C - 1] = room[i + 1][C - 1]
    for i in range(R - 1, airP[1], -1):
        room[i][C - 1] = room[i - 1][C - 1]

    room[airP[0]] = [-1] + room[airP[0]][:-1]
    room[airP[1]] = [-1] + room[airP[1]][:-1]

    room[airP[0]][1] = 0
    room[airP[1]][1] = 0
            

def solution(R, C, T, room):
    airP = ()
    for i in range(R):
        if room[i][0] == -1:
            airP = (i, i + 1)
            break

    for i in range(T):
        spread(R, C, room)
        purify(R, C, airP, room)

    return sum(map(sum, room)) + 2

if __name__ == '__main__':
    R, C, T = map(int, sys.stdin.readline().split())
    room = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

    sys.stdout.write('%d\n'%solution(R, C, T, room))