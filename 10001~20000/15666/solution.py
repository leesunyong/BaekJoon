import sys

read = sys.stdin.readline

def permutation(nums, i, visited, M):
    if M == 0: sys.stdout.write(visited + '\n')
    else :
        for idx in range(i, len(nums)):
            permutation(nums, idx, visited + '%d '%nums[idx], M - 1)


def solution(N, M, nums):
    nums = sorted(nums)
    
    permutation(nums, 0, '', M)


if __name__ == '__main__':
    N, M = map(int, read().split())
    nums = list(set(map(int, read().split())))

    solution(N, M, nums)