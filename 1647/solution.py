import sys

input = sys.stdin.readline

def find(parent, idx):
    
    while parent[idx] != idx:
        idx = parent[idx]

    return idx

def kruskal(num_house, edges):
    """
    Kruskal's Algorithm
    Weighted and Undirected Graph.
    """
    total_weight = 0
    count = 0

    p = list(range(num_house + 1))
    
    for e in edges:
        p_e_0 = find(p, e[0])
        p_e_1 = find(p, e[1])
        
        if p_e_0 != p_e_1:
            count += 1
            total_weight += e[2]

            p[p_e_0] = p[p_e_1] = min(p_e_0, p_e_1)

            if count == num_house - 2:
                break

    return total_weight

N, M = map(int, input().split())
roads = sorted([tuple(map(int, input().split())) for _ in range(M)],
    key=lambda r : r[2])

print(kruskal(N, roads))