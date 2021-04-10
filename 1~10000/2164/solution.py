import sys

def solution(N):
    cards = [i + 1 for i in range(N)]

    while len(cards) > 1:
        if len(cards) % 2 == 0:
            cards = [cards[i] for i in range(1, len(cards), 2)]
        else :
            cards = [cards[i] for i in range(3, len(cards), 2)] + [cards[1]]

    return cards[0]

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    print(solution(N))