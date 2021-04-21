import sys

read = sys.stdin.readline

def solution(N, idx, nums):
    # print(prev, idx)
    answer = [1 for _ in range(N)]

    for i in range(N - 2, -1, -1):
        for j in range(N - 1, i, -1):
            if nums[i] < nums[j]:
                answer[i] = max(answer[i], answer[j] + 1)

    return max(answer)

if __name__ == '__main__':
    N = int(read())
    nums = list(map(int, read().split()))

    sys.stdout.write('%d\n'%solution(N, 0, nums))