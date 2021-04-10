import sys

def solution(N, numbers):
    primes = [2]
    for i in range(2, 1001):
        for p in primes:
            if i % p == 0: break
            elif p * p > i:
                primes.append(i)
                break

    numbers.sort()
    cnt = 0
    for n in numbers:
        if n in primes: cnt += 1

    return cnt

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    numbers = [int(n) for n in sys.stdin.readline().split(' ')]

    print(solution(N, numbers))