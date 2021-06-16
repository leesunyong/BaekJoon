import sys
from math import gcd

MOD = 1_000_000_007

def power(a, b):
    if b == 1: return a
    if b % 2 == 1: return (power(a, b - 1) * a) % MOD
    else :
        r = power(a, b // 2)
        return (r * r) % MOD

def solution(M, dice):
    s = 0

    for d in dice:
        s += d[1] * power(d[0], MOD - 2) % MOD

        if s > MOD:
            s %= MOD

    return s

if __name__ == '__main__':
    M = int(sys.stdin.readline())
    dice = []
    for _ in range(M):
        n, m = map(int, sys.stdin.readline().split())
        g = gcd(n, m)
        n //= g; m //= g

        dice.append((n, m))

    print(solution(M, dice))