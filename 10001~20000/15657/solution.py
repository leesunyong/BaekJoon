import sys

def dfs(result, prev, visited, M, nums):
    if M == 1:
        for i in nums[prev:]:
            result.append(visited + '%d '%i)
    else :
        for i, num in enumerate(nums[prev:]):
            dfs(result, i, visited + '%d '%num, M - 1, nums[prev:])


def solution(N, M, nums):
    result = []
    nums = sorted(nums)

    dfs(result, 0, '', M, nums)

    for r in result:
        sys.stdout.write(r + '\n')
    
if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    solution(N, M, nums)