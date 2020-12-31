N = int(input())
nums = [int(num) for num in input().split(' ')[:N]]
print(min(nums), max(nums))