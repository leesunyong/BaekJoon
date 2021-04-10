import sys

def solution(M, N):
    primes = [2]

    for i in range(2, N + 1):
        for p in primes:
            if i % p == 0: break
            elif p * p > i:
                primes.append(i)
                break
        
    for p in primes:
        if p >= M : sys.stdout.write("%d\n"%p)

if __name__ == '__main__':
    M, N = [int(n) for n in sys.stdin.readline().split(' ')]
    solution(M, N)