def solution(N, array):
    for i, n in enumerate(array):
        for j in range(i):
            print(j)

        for j in range(i + 1, len(array)):
            print(j)

N = input()
array = [int(n) for n in input().split(' ')]
