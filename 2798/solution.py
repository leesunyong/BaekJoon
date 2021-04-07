def solution(N, M, cards):
    maxValue = 0

    for i in range(N):
        for j in range(N):
            if i == j: continue

            for k in range(N):
                if i == k or j == k: continue

                s = cards[i] + cards[j] + cards[k]
                if s <= M and s > maxValue:
                    maxValue = s


    return maxValue

if __name__ == '__main__':
    N, M = [int(n) for n in input().split(' ')]
    cards = [int(c) for c in input().split(' ')]

    print(solution(N, M, cards))