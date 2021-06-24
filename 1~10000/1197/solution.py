import sys

input = sys.stdin.readline

def find(parent, vertex):
    while parent[vertex] != vertex:
        vertex = parent[vertex]

    return vertex

def union(parent, vertex1, vertex2):
    if vertex1 > vertex2:
        parent[vertex2] = vertex1
    else :
        parent[vertex1] = vertex2

def solution(num_vertex, num_edge, edges):
    edges.sort(key=lambda e: e[2])

    parent = list(range(num_vertex + 1))

    count = 0; weight = 0
    for e in edges:
        parent1 = find(parent, e[0])
        parent2 = find(parent, e[1])

        if parent1 != parent2:
            count += 1
            union(parent, parent1, parent2)

            weight += e[2]

            if count == num_vertex - 1: break

    return weight

V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append(tuple(map(int, input().split())))

print(solution(V, E, edges))