def solution(N, prices):
    values = [0, 0, 0] # R, G, B
    
    for p in prices:
        values = [min([values[1] + p[0], values[2] + p[0]]), min([values[0] + p[1], values[2] + p[1]]), min([values[0] + p[2], values[1] + p[2]])]

    return min(values)

if __name__ == '__main__':
    N = int(input())
    prices = []
    for _ in range(N):
        line = [int(p) for p in input().split(' ')]
        prices.append(line)

    print(solution(N, prices))