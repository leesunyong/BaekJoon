import sys

def solution(P):
    P.sort()
    sum = 0
    waiting = 0
    for p in P:
        sum += waiting + p
        waiting += p

    return sum

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    P = [int(n) for n in sys.stdin.readline().split(' ')]
    print(solution(P))