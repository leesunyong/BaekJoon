import sys

def solution(n, nums, idx):
    if n == 1:
        if nums[0][0] > nums[1][0]: return nums[0][0]
        else : return nums[1][0]

    if idx == -1:
        

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        nums = map(int, sys.stdin.readline().split())

        sys.stdout.write('%d\n'%solution(n, nums, -1))