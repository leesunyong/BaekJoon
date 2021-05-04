import sys
from itertools import combinations

input = sys.stdin.readline

def solution(M, house, chicken):
    cDis = [[abs(h[0] - c[0]) + abs(h[1] - c[1]) for c in chicken] for h in house]
    
    cityDis = 2500
    for i in combinations((j for j in range(len(chicken))), M):
        dis = 0
        for k in range(len(cDis)):
            dis += min([cDis[k][c] for c in i])
        cityDis = min(cityDis, dis)

    return cityDis

if __name__ == '__main__':
    N, M = map(int, input().split())

    city = []; house = []; chicken = []
    for i in range(N):
        city.append(input().split())
        for j in range(N):
            if city[i][j] == '1': house.append((i, j))
            elif city[i][j] == '2': chicken.append((i, j))
    print(solution(M, house, chicken))