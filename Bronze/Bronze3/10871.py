N, X = [int(num) for num in input().split(' ')[:2]]
nums = input().split(' ')[:N]

for num in nums:
    if int(num) < X:
        print(num, end=' ')

print('')