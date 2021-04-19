nums = [int(num) % 10 for num in input().split(' ')[:5]]
verification = 0
for num in nums:
    verification += num * num
print(verification % 10)