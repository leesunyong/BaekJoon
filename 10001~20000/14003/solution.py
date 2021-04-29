import sys
import bisect

read = sys.stdin.readline

def solution(nums):
    lis = [nums[0]];length = 1
    cnt = [0]
    for n in nums[1:]:
        if n > lis[length - 1]:
            lis.append(n)
            cnt.append(length)
            length += 1
        else :
            idx = bisect.bisect_left(lis, n)
            lis[idx] = n
            cnt.append(idx)

    answer = []
    sys.stdout.write('%d\n'%length)
    for idx in range(len(cnt) - 1, -1, -1):
        if cnt[idx] == length - 1:
            answer.append(nums[idx])
            length -= 1

    sys.stdout.write('%s\n'%(' '.join([str(a) for a in answer[::-1]])))


if __name__ == '__main__':
    N = int(read())
    nums = list(map(int, read().split()))

    solution(nums)