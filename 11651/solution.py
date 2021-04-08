def solution(N, coords):
    coords = sorted(coords, key = lambda coord : (coord[1], coord[0]))
    
    for c in coords:
        print(c[0], c[1])

if __name__ == '__main__':
    N = int(input())
    coords = []
    for i in range(N):
        x, y = input().split(' ')
        coords.append((int(x), int(y)))

    solution(N, coords)