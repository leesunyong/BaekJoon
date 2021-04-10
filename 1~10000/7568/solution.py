def solution(N, heightWeight):
    rank = [1 for _ in range(N)]

    for i, (h, w) in enumerate(heightWeight):
        for h1, w1 in heightWeight:
            if h1 > h and w1 > w:
                rank[i] += 1

    rank = [str(r) for r in rank]
    print(' '.join(rank))

if __name__ == '__main__':
    N = int(input())
    heightWeight = []
    for _ in range(N):
        h, w = input().split(' ')
        heightWeight.append((int(h), int(w)))

    solution(N, heightWeight)