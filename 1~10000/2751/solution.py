import sys

def solution(N, numbers):
    for i, n in enumerate(numbers):
        if n: sys.stdout.write('%d\n'%(i - 1000000))


if __name__ == '__main__':
    N = int(input())
    numbers = [False for _ in range(2000001)]
    for i in range(N):
        numbers[int(sys.stdin.readline()) + 1000000] = True
    solution(N, numbers)