import sys

def solution(N, numbers):
    for i, n in enumerate(numbers):
        sys.stdout.write(('%d\n'%i)*n)

if __name__ == '__main__':
    N = int(input())
    numbers = [0 for _ in range(10001)]
    for i in range(N):
        numbers[int(sys.stdin.readline())] += 1

    solution(N, numbers)