import sys
sys.setrecursionlimit(40000)

def GCD(a,b):
    if a > b:
        if a % b == 0 : return b
        else : return GCD(b, a - b)
    else :
        if b % a == 0 : return a
        else : return GCD(a, b - a)

def solution(T, testCase):
    for t in testCase:
        M, N, x, y = t

        maxYear = M * N // GCD(M, N)
        while True:
            if x == y :
                sys.stdout.write('%d\n'%x)
                break

            if x > y : y += N
            else : x += M

            if x > maxYear or y > maxYear:
                sys.stdout.write('-1\n')
                break

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    testCase = [[int(n) for n in sys.stdin.readline().split(' ')] for _ in range(T)]

    solution(T, testCase)