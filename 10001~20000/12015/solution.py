import sys
import bisect

read = sys.stdin.readline

def solution(nums):
    lis = [nums[0]];length = 1
    for n in nums[1:]:
        if n > lis[length - 1]:
            lis.append(n)
            length += 1
        else :
            idx = bisect.bisect_left(lis, n)
            lis[idx] = n

    sys.stdout.write('%d\n'%length)

if __name__ == '__main__':
    N = int(read())
    nums = list(map(int, read().split()))

    solution(nums)