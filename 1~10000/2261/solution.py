import sys

def distance(N, dots):
    return N

def solution(N, dots):
    return N

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    dots = []
    for i in range(N):
        dots.append([int(n) for n in sys.stdin.readline().split(' ')])

    print(solution(N, dots))