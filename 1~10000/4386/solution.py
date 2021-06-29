from itertools import combinations

def find(parent, a):
    while parent[a] != a:
        a = parent[a]

    return a

def solution(n, stars):    
    distance = []

    for i, j in combinations(range(n), 2):
        distance.append((((stars[i][0] - stars[j][0]) ** 2 +(stars[i][1] - stars[j][1]) ** 2) ** 0.5,i,j))

    distance.sort(key=lambda d: d[0])

    total_distance = 0
    parent = [i for i in range(n)]
    
    for dis, x, y in distance:
        parent_0 = find(parent, x)
        parent_1 = find(parent, y)

        if parent_0 != parent_1:
            parent[parent_0] = parent_1
            total_distance += dis

    return total_distance

n = int(input())

print('%.2f'%solution(n, [tuple(map(float, input().split())) for _ in range(n)]))