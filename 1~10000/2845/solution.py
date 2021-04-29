import sys

L, P = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
n = L * P
for i in range(len(nums)):
    nums[i] -= n

sys.stdout.write('%s\n'%(' '.join([str(c) for c in nums])))