import sys

read = sys.stdin.readline
write = sys.stdout.write

def permutation(visited, nums, N, M, per):
    if M == 0: write(per + '\n')
    else :
        prev = -1
        for i in range(N):
            if prev != nums[i]: 
                if not visited[i]:
                    visited[i] = True
                    permutation(visited, nums, N, M - 1, per + '%d '%nums[i])
                    visited[i] = False

                    prev = nums[i]

def solution(N, M, nums):
    visited = [False for _ in range(N)]
    nums = sorted(nums)

    permutation(visited, nums, N, M, '')


if __name__ == '__main__':
    N, M = map(int, read().split())
    nums = list(map(int, read().split()))

    solution(N, M, nums)