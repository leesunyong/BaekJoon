import sys

def dfs(result, visited, M, nums):
    if M == 1:
        for i in nums:
            if not i in visited:
                result.append(visited + [i])
    else :
        for i in nums:
            if not i in visited:
                dfs(result, visited + [i], M - 1, nums)


def solution(N, M, nums):
    # Combination
    result = []; visited = []
    nums = sorted(nums)

    dfs(result, visited, M, nums)

    for r in result:
        sys.stdout.write(' '.join([str(s) for s in r]) + '\n')
    
if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
    solution(N, M, nums)