import sys

def solution(numbers, ranges):
    sum = 0
    for i, n in enumerate(numbers):
        sum += n
        numbers[i] = sum

    for r in ranges:
        sys.stdout.write(str(numbers[r[1]] - numbers[r[0] - 1]) + '\n')

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    numbers = [0] + [int(n) for n in sys.stdin.readline().split(' ')]
    ranges = []
    for i in range(1, M + 1):
        ranges.append([int(n) for n in sys.stdin.readline().split(' ')])

    solution(numbers, ranges)
