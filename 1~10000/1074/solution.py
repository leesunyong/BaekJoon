import sys

def solution(N, r, c):
    digit = 2 ** (N - 1)
    answer = 0
    while digit > 0:
        answer += (2 * (r // digit) + c // digit) * digit * digit
        r %= digit
        c %= digit
        digit //= 2
        

    return answer

if __name__ == '__main__':
    N, r, c = map(int, sys.stdin.readline().split())

    sys.stdout.write('%d\n'%solution(N, r, c))