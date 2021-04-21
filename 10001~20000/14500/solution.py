import sys

def solution(N, M, numbers):
    maxSum = 0
    nums = [[0 for _ in range(M + 6)] for _ in range(N + 6)]
    for i in range(N):
        for j in range(M):
            nums[i + 3][j + 3] = numbers[i][j]

    next = [[(0, 1), (0, 2), (0, 3)],
            [(1, 0), (0, 1), (1, 1)],
            [(0, 1), (1, 1), (0, 2)],
            [(0, 1), (-1, 1), (0, 2)],
            [(1, 0), (1, 1), (2, 1)],
            [(1, 0), (1, -1), (2, -1)],
            [(1, 0), (2, 0), (2, 1)],
            [(1, 0), (2, 0), (2, -1)]]

    for i in range(N):
        for j in range(M):
            for n in next:
                tmp1 = tmp2 = tmp3 = tmp4 = numbers[i][j]
                for b in n:
                    tmp1 += nums[b[0] + i + 3][b[1] + j + 3]
                    tmp2 += nums[b[1] + i + 3][b[0] + j + 3]
                    tmp3 += nums[-b[0] + i + 3][-b[1] + j + 3]
                    tmp4 += nums[-b[1] + i + 3][-b[0] + j + 3]
                
                if tmp1 > maxSum: maxSum = tmp1
                if tmp2 > maxSum: maxSum = tmp2
                if tmp3 > maxSum: maxSum = tmp3
                if tmp4 > maxSum: maxSum = tmp4

    return maxSum

if __name__ == '__main__':
    N, M = [int(n) for n in sys.stdin.readline().split(' ')]
    numbers = []
    for _ in range(N):
        numbers.append([int(n) for n in sys.stdin.readline().split(' ')])

    print(solution(N, M, numbers))