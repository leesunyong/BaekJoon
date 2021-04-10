def solution(N):

    d = 1
    start = 2
    while True:
        if start > N:
            return d
        start += 6 * d
        d += 1

if __name__ == '__main__':
    N = int(input())

    print(solution(N))