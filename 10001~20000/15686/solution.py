import sys

def dp(dis, i, M):
    if M == len(dis[0]) - i:
        return sum(map(min, dis))
    else :
        

def solution(N, M, city):
    house = []; chicken = []
    for i, c in enumerate(city):
        for j, s in enumerate(c):
            if s == 1: house.append((i, j))
            elif s == 2: chicken.append((i, j))
    
    dis = [[0] * len(chicken) for _ in range(len(house))]

    for i, h in enumerate(house):
        for j, c in enumerate(chicken):
            dis[i][j] = abs(h[0] - c[0]) + abs(h[1] - c[1])

    dp(dis, 0, M)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    solution(N, M, city)