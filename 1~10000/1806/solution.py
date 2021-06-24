def solution(nums, N, s):
    min_length = 100_001
    sum_val = 0
    start = 0
    
    for i in range(N):
        sum_val += nums[i]
        while sum_val - nums[start] >= s:
            sum_val -= nums[start]
            start += 1
        if sum_val >= s and min_length > i - start + 1:
            min_length = i - start + 1

    if min_length == 100_001: return 0
    else : return min_length

N, S = map(int, input().split())
nums = list(map(int, input().split()))

print(solution(nums, N, S))