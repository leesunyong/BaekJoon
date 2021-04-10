import sys

def solution(N, M, cards, counts):
    cardCounts = {}
    for c in cards:
        if c in cardCounts.keys():
            cardCounts[c] += 1
        else :
            cardCounts[c] = 1

    answer = [0 for _ in counts]
    for i in range(M):
        if counts[i] in cardCounts.keys():
            answer[i] = cardCounts[counts[i]]
        

    print(' '.join([str(a) for a in answer]))

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    cards = [int(c) for c in sys.stdin.readline().split(' ')]

    M = int(sys.stdin.readline())
    counts = [int(c) for c in sys.stdin.readline().split(' ')]

    solution(N, M, cards, counts)