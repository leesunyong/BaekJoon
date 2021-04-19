import sys

def solution(n, m):
    answer = 1
    per = 1
    for i in range(m):
        answer *= (n - i)
        per *= (m - i)

    return answer // per

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(solution(n, m)) + '\n')